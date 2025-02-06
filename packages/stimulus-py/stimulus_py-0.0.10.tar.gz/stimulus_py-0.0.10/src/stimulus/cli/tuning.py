#!/usr/bin/env python3

import argparse
import json
import os
import yaml
import safetensors

from torch.utils.data import DataLoader
from stimulus.utils.launch_utils import import_class_from_file, get_experiment, memory_split_for_ray_init
from stimulus.learner.raytune_learner import TuneWrapper as StimulusTuneWrapper
from stimulus.learner.raytune_parser import TuneParser as StimulusTuneParser
from stimulus.data.handlertorch import TorchDataset
from stimulus.learner.predict import PredictWrapper


def get_args():

    "get the arguments when using from the commandline"
    
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-c", "--config", type=str, required=True, metavar="FILE", help='The file path for the config file')
    parser.add_argument("-m", "--model", type=str, required=True, metavar="FILE", help='The model file')
    parser.add_argument("-d", "--data", type=str, required=True, metavar="FILE", help='The data file')
    parser.add_argument("-e", "--experiment_config", type=str, required=True, metavar="FILE", help='The json used to modify the data. Inside it has the experiment name as specified in the experimets.py, this will then be dinamically imported during training. It is necessary to recover how the user specified the encoding of the data. Data is encoded on the fly.')
    parser.add_argument("-o", "--output", type=str, required=False,  nargs='?', const='best_model.pt', default='best_model.pt', metavar="FILE", help='The output file path to write the trained model to')
    parser.add_argument("-bc", "--best_config", type=str, required=False, nargs='?', const='best_config.json', default='best_config.json', metavar="FILE", help='The path to write the best config to')
    parser.add_argument("-bm", "--best_metrics", type=str, required=False, nargs='?', const='best_metrics.csv', default='best_metrics.csv', metavar="FILE", help='The path to write the best metrics to')
    parser.add_argument("-bo", "--best_optimizer", type=str, required=False, nargs='?', const='best_optimizer.pt', default='best_optimizer.pt', metavar="FILE", help='The path to write the best optimizer to')
    parser.add_argument("-w", "--initial_weights", type=str, required=False, nargs='?', const=None, default=None,  metavar="FILE", help='The path to the initial weights. These can be used by the model instead of the random initialization')
    parser.add_argument("--gpus", type=int, required=False, nargs='?', const=None, default=None, metavar="NUM_OF_MAX_GPU", help="Use to limit the number of GPUs ray can use. This might be useful on many occasions, especially in a cluster system. The default value is None meaning ray will use all GPUs available. It can be set to 0 to use only CPUs.")
    parser.add_argument("--cpus", type=int, required=False, nargs='?', const=None, default=None, metavar="NUM_OF_MAX_CPU", help="Use to limit the number of CPUs ray can use. This might be useful on many occasions, especially in a cluster system. The default value is None meaning ray will use all CPUs available. It can be set to 0 to use only GPUs.")
    parser.add_argument("--memory", type=str, required=False, nargs='?', const=None, default=None, metavar="MAX_MEMORY", help="ray can have a limiter on the total memory it can use. This might be useful on many occasions, especially in a cluster system. The default value is None meaning ray will use all memory available.")
    parser.add_argument("--ray_results_dirpath", type=str, required=False, nargs='?', const=None, default=None, metavar="DIR_PATH", help="the location where ray_results output dir should be written. if set to None (default) ray will be place it in ~/ray_results ")
    parser.add_argument("--tune_run_name", type=str, required=False, nargs='?', const=None, default=None, metavar="CUSTOM_RUN_NAME", help="tells ray tune what that the 'experiment_name' aka the given tune_run name should be. This is controlled be the variable name in the RunConfig class of tune. This has two behaviuors: 1 if set the subdir of ray_results is going to be named with this value, 2 the subdir of the above mentioned will also have this value as prefix for the single train dir name. Default None, meaning ray will generate such a name on its own.")
    parser.add_argument("--debug_mode", type=str, required=False, nargs='?', const=False, default=False, metavar="DEV", help="activate debug mode for tuning. default false, no debug.")

    args = parser.parse_args()
        
    return args

def main(config_path: str,
         model_path: str,
         data_path: str,
         experiment_config: str,
         output: str,
         best_config_path: str,
         best_metrics_path: str,
         best_optimizer_path: str,
         initial_weights_path: str = None,
         gpus: int = None,
         cpus: int = None,
         memory: str = None,
         ray_results_dirpath: str = None,
         tune_run_name: str = None,
         _debug_mode: str = False) -> None:
    """
    This launcher use ray tune to find the best hyperparameters for a given model.
    """

    # TODO update to yaml the experiment config
    # load json into dictionary
    exp_config = {}
    with open(experiment_config, 'r') as in_json:
        exp_config = json.load(in_json)

    # initialize the experiment class
    initialized_experiment_class = get_experiment(exp_config["experiment"])

    # import the model correctly but do not initialize it yet, ray_tune does that itself
    model_class = import_class_from_file(model_path)

    # Update the tune config file. Because if resources are specified for cpu and gpu they are overwritten with what nextflow has otherwise this field is created
    updated_tune_conf = "check_model_modified_tune_config.yaml"
    with open(config_path, 'r') as conf_file, open(updated_tune_conf, "w") as new_conf:
        user_tune_config = yaml.safe_load(conf_file)

        # add initial weights to the config, when provided
        if initial_weights_path is not None:
            user_tune_config["model_params"]["initial_weights"] = os.path.abspath(initial_weights_path)
        
        # save to file the new dictionary because StimulusTuneWrapper only takes paths
        yaml.dump(user_tune_config, new_conf)

    # compute the memory requirements for ray init. Usefull in case ray detects them wrongly. Memory is split in two for ray: for store_object memory and the other actual memory for tuning. The following function takes the total possible usable/allocated memory as a string parameter and return in bytes the values for store_memory (30% as default in ray) and memory (70%).
    object_store_mem, mem = memory_split_for_ray_init(memory)

    # set ray_result dir ubication. TODO this version of pytorch does not support relative paths, in future maybe good to remove abspath.
    ray_results_dirpath = None if ray_results_dirpath is None else os.path.abspath(ray_results_dirpath)

    # Create the learner
    learner = StimulusTuneWrapper(updated_tune_conf,
                                  model_class,
                                  data_path,
                                  initialized_experiment_class,
                                  max_gpus=gpus,
                                  max_cpus=cpus,
                                  max_object_store_mem=object_store_mem,
                                  max_mem=mem,
                                  ray_results_dir=ray_results_dirpath,
                                  tune_run_name=tune_run_name,
                                  _debug=_debug_mode) 
    
    # Tune the model and get the tuning results
    grid_results = learner.tune()

    # parse raytune results
    results = StimulusTuneParser(grid_results)
    results.save_best_model(output)
    results.save_best_config(best_config_path)
    results.save_best_metrics_dataframe(best_metrics_path)
    results.save_best_optimizer(best_optimizer_path)

    # debug section. predict the validation data using the best model.
    if _debug_mode:
        # imitialize the model class with the respective tune parameters from the associated config
        best_tune_config = results.get_best_config()
        best_model = model_class(**best_tune_config["model_params"])
        # get the weights associated to the best model and load them onto the model class
        best_model.load_state_dict(results.get_best_model())
        # load the data in a dataloader and then predict them in an ordered manner, aka no shuffle.
        validation_set = DataLoader(TorchDataset(data_path, initialized_experiment_class, split=1), batch_size=learner.config['data_params']['batch_size'].sample(), shuffle=False)
        predictions = PredictWrapper(best_model, validation_set).predict()
        # write to file the predictions, in the ray result tune specific folder. 
        pred_filename = os.path.join(learner.config["tune_run_path"], "debug", "best_model_val_pred.txt")
        # save which was the best model found, the easiest is to get its seed
        best_model_seed = os.path.join(learner.config["tune_run_path"], "debug", "best_model_seed.txt")
        with open(pred_filename, 'w') as pred_f, open(best_model_seed, 'w') as seed_f:
            pred_f.write(str(predictions))
            seed_f.write(str(best_tune_config['ray_worker_seed'])) 

def run():
    args = get_args()
    main(args.config, 
         args.model, 
         args.data, 
         args.experiment_config, 
         args.output, 
         args.best_config, 
         args.best_metrics, 
         args.best_optimizer,
         args.initial_weights,
         args.gpus,
         args.cpus,
         args.memory,
         args.ray_results_dirpath,
         args.tune_run_name,
         args.debug_mode)


if __name__ == "__main__":
    run()

