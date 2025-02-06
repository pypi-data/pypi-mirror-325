import os
import ray.tune.schedulers as schedulers
import torch
import torch.nn as nn
import torch.optim as optim 
import random
import numpy as np
import datetime

from ray import train, tune, cluster_resources, init, is_initialized, shutdown
from ray.tune import Trainable
from torch.utils.data import DataLoader
from ..data.handlertorch import TorchDataset
from ..utils.yaml_model_schema import YamlRayConfigLoader
from ..utils.generic_utils import set_general_seeds
from .predict import PredictWrapper
from typing import Tuple

from safetensors.torch import load_file as safe_load_file
from safetensors.torch import save_file as safe_save_file
from safetensors.torch import load_model as safe_load_model
from safetensors.torch import save_model as safe_save_model


class TuneWrapper():
    def __init__(self,
                 config_path: str,
                 model_class: nn.Module,
                 data_path: str,
                 experiment_object: object,
                 max_gpus: int = None,
                 max_cpus: int = None,
                 max_object_store_mem: float = None,
                 max_mem: float = None,
                 ray_results_dir: str = None,
                 tune_run_name: str = None,
                 _debug: str = False) -> None:
        """
        Initialize the TuneWrapper with the paths to the config, model, and data.
        """
        self.config = YamlRayConfigLoader(config_path).get_config()

        # set all general seeds: python, numpy and torch.
        set_general_seeds(self.config["seed"])

        self.config["model"] = model_class
        self.config["experiment"] = experiment_object

        # add the ray method for number generation to the config so it can be passed to the trainable class, that will in turn set per worker seeds in a reproducible mnanner.
        self.config["ray_worker_seed"] = tune.randint(0, 1000)

        # add the data path to the config so it know where it is during tuning
        if not os.path.exists(data_path):
            raise ValueError("Data path does not exist. Given path:" + data_path)
        self.config["data_path"] = os.path.abspath(data_path)
        
        # build the tune config
        self.config["tune"]["tune_params"]["scheduler"] = getattr(schedulers, self.config["tune"]["scheduler"]["name"])( **self.config["tune"]["scheduler"]["params"])
        self.tune_config = tune.TuneConfig(**self.config["tune"]["tune_params"])

        # set ray cluster total resources (max)
        self.max_gpus             = max_gpus
        self.max_cpus             = max_cpus
        self.max_object_store_mem = max_object_store_mem     # this is a special subset of the total usable memory that ray need for his internal work, by default is set to 30% of total memory usable
        self.max_mem              = max_mem

        # build the run config
        self.checkpoint_config = train.CheckpointConfig(checkpoint_at_end=True) #TODO implement checkpoiting
        # in case a custom name was not given for tune_run_name, build it like ray would do. to later pass it on the worker for the debug section.
        if tune_run_name is None:
            tune_run_name = "TuneModel_" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.run_config = train.RunConfig(name=tune_run_name,
            storage_path=ray_results_dir,
            checkpoint_config=self.checkpoint_config,
            **self.config["tune"]["run_params"]
                                        )                                       #TODO maybe put name into config if it was possible to retrieve from tune the name of the result subdir)

        # working towards the path for the tune_run directory. if ray_results_dir None ray will put it under home so we will do the same here.
        if ray_results_dir is None:
            ray_results_dir = os.environ.get("HOME")
        # then we are able to pass the whole correct tune_run path to the trainable function. so it can use thaqt to place the debug dir under if needed.
        self.config["tune_run_path"] = os.path.join(ray_results_dir, tune_run_name)

        # pass the debug flag to the config taken fromn tune so it can be used inside the setup of the trainable
        self.config["_debug"] = False
        if _debug:
            self.config["_debug"] = True

        self.tuner = self.tuner_initialization()


    def tuner_initialization(self) -> tune.Tuner:
        """
        Prepare the tuner with the configs.
        """

        # in ray 3.0.0 the following issue is fixed. Sometimes it sees that ray is already initialized, so in that case shut it off and start anew. TODO update to ray 3.0.0
        if is_initialized():
            shutdown()

        # initialize the ray cluster with the limiter on CPUs, GPUs or memory if needed, otherwise everything that is available. None is what ray uses to get all resources available for either CPU, GPU or memory.
        # memory is split in two for ray. read more at ray.init documentation.
        init(num_cpus=self.max_cpus,
             num_gpus=self.max_gpus,
             object_store_memory=self.max_object_store_mem,
             _memory=self.max_mem,
            )

        print("CLUSTER resources   ->  ", cluster_resources())

        # check if resources per trial are not exceeding maximum resources. traial = single set/combination of hyperparameter (parrallel actors maximum resources in ray tune gergon).
        self.gpu_per_trial = self._chek_per_trial_resources("gpu_per_trial", cluster_resources(), "GPU")
        self.cpu_per_trial = self._chek_per_trial_resources("cpu_per_trial", cluster_resources(), "CPU")
        
        print("PER_TRIAL resources ->  GPU:", self.gpu_per_trial, "CPU:", self.cpu_per_trial )

        # wrap the trainable with the allowed resources per trial
        # also provide the training and validation data to the trainable through with_parameters
        # this is a wrapper that passes the data as a object reference (pointer)
        trainable = tune.with_resources(TuneModel, resources={"cpu": self.cpu_per_trial, "gpu": self.gpu_per_trial})
        trainable = tune.with_parameters(trainable,
                                         training = TorchDataset(self.config["data_path"], self.config["experiment"], split=0),
                                         validation = TorchDataset(self.config["data_path"], self.config["experiment"], split=1))

        return tune.Tuner(trainable,
                          tune_config=self.tune_config,
                          param_space=self.config,
                          run_config=self.run_config)

    def tune(self) -> None:
        """
        Run the tuning process.
        """

        return self.tuner.fit()

    def _chek_per_trial_resources(self, resurce_key: str,  cluster_max_resources: dict, resource_type: str) -> Tuple[int, int] :
        """
        Helper function that check that user requested per trial resources are not exceeding the available resources for the ray cluster.
        If the per trial resources are not asked they are set to a default resoanable ammount.
        
        resurce_key:            str object          the key used to look into the self.config["tune"]
        cluster_max_resources:  dict object         the output of the ray.cluster_resources() function. It hold what ray has found to be the available resources for CPU, GPU and Memory
        resource_type:          str object          the key used to llok into the cluster_resources dict 
        """
        
        if resource_type == "GPU" and resource_type not in cluster_resources().keys():
            # ray does not have a GPU field also if GPUs were set to zero. So trial GPU resources have to be set to zero.
            if self.max_gpus == 0:
                return 0.0
            # in case GPUs that are not detected raise error. This happens sometimes when max_gpus stay as None and ray.init does not find GPU by itself. not setting max_gpus (None) means to use all available ones. TODO make ray see GPU on None value.
            else:
                raise SystemError("#### ray did not detect any GPU, if you do not want to use GPU set max_gpus=0, or in nextflow --max_gpus 0.")

        per_trial_resource = None
        # if everything is alright, leave the value as it is.
        if resurce_key in self.config["tune"].keys() and self.config["tune"][resurce_key] <= cluster_max_resources[resource_type]:
            per_trial_resource = self.config["tune"][resurce_key]

        # if per_trial_resource are more than what is avaialble to ray set them to what is available and warn the user
        elif resurce_key in self.config["tune"].keys() and self.config["tune"][resurce_key] > cluster_max_resources[resource_type]:
            # TODO write a better warning
            print("\n\n####   WARNING  - ", resource_type, "per trial are more than what is available.", resource_type, " per trial :", self.config["tune"][resurce_key], "available :", cluster_max_resources[resource_type], "overwrting value to max avaialable" )
            per_trial_resource = cluster_max_resources[resource_type]
        
        # if per_trial_resource has not been asked and there is none available set them to zero
        elif resurce_key not in self.config["tune"].keys() and cluster_max_resources[resource_type] == 0.0:
            per_trial_resource = 0
        
        # if per_trial_resource has not been asked and the resource is available set the value to either 1 or number_available resource / num_samples
        elif resurce_key not in self.config["tune"].keys() and cluster_max_resources[resource_type] != 0.0:
            # TODO maybe set the default to 0.5 instead of 1 ? fractional use in case of GPU? Should this be a mandatory parameter?
            per_trial_resource = max(1, (cluster_max_resources[resource_type] // self.config["tune"]["tune_params"]["num_samples"] ))

        return per_trial_resource
    

class TuneModel(Trainable):

    def setup(self, config: dict, training: object, validation: object) -> None:
        """
        Get the model, loss function(s), optimizer, train and test data from the config.
        """

        # set the seeds the second time, first in TuneWrapper initialization. This will make all important seed worker specific.
        set_general_seeds(self.config["ray_worker_seed"])

        # Initialize model with the config params
        self.model = config["model"](**config["model_params"])

        # Add data path
        self.data_path = config["data_path"]

        # Get the loss function(s) from the config model params
        # Note that the loss function(s) are stored in a dictionary, 
        # where the keys are the key of loss_params in the yaml config file and the values are the loss functions associated to such keys.
        self.loss_dict = config["loss_params"]
        for key, loss_fn in self.loss_dict.items():
            try:
                self.loss_dict[key] = getattr(nn, loss_fn)()
            except AttributeError:
                raise ValueError(f"Invalid loss function: {loss_fn}, check PyTorch for documentation on available loss functions")

        # get the optimizer parameters
        optimizer_lr = config["optimizer_params"]["lr"]

        # get the optimizer from PyTorch
        self.optimizer = getattr(optim, config["optimizer_params"]["method"])(self.model.parameters(), lr=optimizer_lr)

        # get step size from the config
        self.step_size = config["tune"]['step_size']

        # use dataloader on training/validation data
        self.batch_size = config['data_params']['batch_size']
        self.training = DataLoader(training, batch_size=self.batch_size, shuffle=True)  # TODO need to check the reproducibility of this shuffling
        self.validation = DataLoader(validation, batch_size=self.batch_size, shuffle=True)

        # debug section, first create a dedicated directory for each worker inside Ray_results/<tune_model_run_specific_dir> location
        debug_dir = os.path.join(config["tune_run_path"], "debug", ("worker_with_seed_" + str(self.config["ray_worker_seed"])))
        if config["_debug"]:
            # creating a special directory for it one that is worker/trial/experiment specific
            os.makedirs(debug_dir)
            seed_filename = os.path.join(debug_dir, "seeds.txt")

            # save the initialized model weights
            self.export_model(export_dir=debug_dir)

            # save the seeds
            with open(seed_filename, 'a') as seed_f:
                # you can not retrieve the actual seed once it set, or the current seed neither for python, numpy nor torch. so we select five numbers randomly. If that is the first draw of numbers they are always the same.
                python_values = random.sample(range(100), 5)
                numpy_values = list(np.random.randint(0, 100, size=5))
                torch_values = torch.randint(0, 100, (5,)).tolist()
                seed_f.write(f"python drawn numbers : {python_values}\nnumpy drawn numbers : {numpy_values}\ntorch drawn numbers : {torch_values}\n")


        

    def step(self) -> dict:
        """
        For each batch in the training data, calculate the loss and update the model parameters.
        This calculation is performed based on the model's batch function.
        At the end, return the objective metric(s) for the tuning process.
        """

        for step_size in range(self.step_size):
            for x, y, meta in self.training:
                # the loss dict could be unpacked with ** and the function declaration handle it differently like **kwargs. to be decided, personally find this more clean and understable.
                self.model.batch(x=x, y=y, optimizer=self.optimizer, **self.loss_dict)
        return self.objective()

    def objective(self) -> dict:
        """
        Compute the objective metric(s) for the tuning process.
        """

        metrics = ['loss', 'rocauc', 'prauc', 'mcc', 'f1score', 'precision', 'recall', 'spearmanr']  # TODO maybe we report only a subset of metrics, given certain criteria (eg. if classification or regression)
        predict_val = PredictWrapper(self.model, self.validation, loss_dict=self.loss_dict)
        predict_train = PredictWrapper(self.model, self.training, loss_dict=self.loss_dict)
        return {**{'val_'+metric : value for metric,value in predict_val.compute_metrics(metrics).items()},
                **{'train_'+metric : value for metric,value in predict_train.compute_metrics(metrics).items()}}

    def export_model(self, export_dir: str) -> None:
        safe_save_model(self.model, os.path.join(export_dir,  "model.safetensors"))

    def load_checkpoint(self, checkpoint_dir: str) -> None:
        self.model = safe_load_model(self.model, os.path.join(checkpoint_dir, "model.safetensors"))
        self.optimizer.load_state_dict(torch.load(os.path.join(checkpoint_dir, "optimizer.pt")))

    def save_checkpoint(self, checkpoint_dir: str) -> dict | None:
        safe_save_model(self.model, os.path.join(checkpoint_dir, "model.safetensors"))
        torch.save(self.optimizer.state_dict(), os.path.join(checkpoint_dir, "optimizer.pt"))
        return checkpoint_dir
    
