import unittest
import os
import shutil
import torch
from src.stimulus.data.experiments import DnaToFloatExperiment
from src.stimulus.learner.raytune_learner import TuneModel
from tests.test_model.dnatofloat_model import ModelSimple
from src.stimulus.learner.raytune_learner import TuneWrapper 
from src.stimulus.utils.yaml_model_schema import YamlRayConfigLoader
from torch.utils.data import DataLoader
from src.stimulus.data.handlertorch import TorchDataset


class TestTuneWrapper(unittest.TestCase):
    def setUp(self):
        config_path = "bin/tests/test_model/dnatofloat_model_cpu.yaml"
        model_class = ModelSimple
        experiment_obj = DnaToFloatExperiment()
        data_path = "bin/tests/test_data/dna_experiment/test_with_split.csv"
        self.wrapper = TuneWrapper(config_path,
                                   model_class,
                                   data_path,
                                   experiment_obj,
                                   max_cpus=2,
                                   max_gpus=0,
                                   )
    
    def test_setup(self):
        self.assertIsInstance(self.wrapper.config, dict)
        self.assertTrue(self.wrapper.tune_config is not None)
        self.assertTrue(self.wrapper.checkpoint_config is not None)
        self.assertTrue(self.wrapper.run_config is not None)
        self.assertTrue(self.wrapper.tuner is not None)
    
    def test_tune(self):
        result_grid = self.wrapper.tune()
        self.assertTrue(result_grid is not None)
        # checking that every run of tune ended with no errors
        for i in range(len(result_grid)):
            result = result_grid[i]
            self.assertTrue(result.error is None)

# this test here is avoided, because one cannot call TuneModel(config, training, validation) directly
# TODO find a way to test the TuneModel setup
# class TestTuneModel(unittest.TestCase):
#     def setUp(self):
#         torch.manual_seed(1234)
#         config = YamlRayConfigLoader("bin/tests/test_model/simple_config.yaml").get_config_instance()
#         config["model"] = ModelSimple
#         config["experiment"] = DnaToFloatExperiment()
#         config["data_path"] = "bin/tests/test_data/dna_experiment/test_with_split.csv"
#         training = TorchDataset(config["data_path"], config["experiment"], split=0)
#         validation = TorchDataset(config["data_path"], config["experiment"], split=1)
#         self.learner = TuneModel(config = config, training = training, validation = validation)

#     def test_setup(self):
#         self.assertIsInstance(self.learner.loss_dict, dict)
#         self.assertTrue(self.learner.optimizer is not None)
#         self.assertIsInstance(self.learner.training, DataLoader)
#         self.assertIsInstance(self.learner.validation, DataLoader) 

#     # def test_step(self):
#     #     #torch.manual_seed(1234)
#     #     self.learner.step()
#     #     test_data = next(iter(self.learner.training))[0]["hello"]
#     #     test_output = self.learner.model(test_data)
#     #     test_output = round(test_output.item(),4)
#     #     #self.assertEqual(test_output, 0.4547) -> seed seems to be braking (random is not deterministic)

#     # def test_objective(self):
#     #     obj = self.learner.objective()
#     #     self.assertIsInstance(obj, dict)
#     #     self.assertTrue("val_loss" in obj.keys())
#     #     self.assertIsInstance(obj["val_loss"], float)

#     def test_export_model(self):
#         self.learner.export_model("bin/tests/test_data/dna_experiment/test_model.pth")
#         self.assertTrue(os.path.exists("bin/tests/test_data/dna_experiment/test_model.pth"))
#         os.remove("bin/tests/test_data/dna_experiment/test_model.pth")
    
#     def test_save_checkpoint(self):
#         checkpoint_dir = "bin/tests/test_data/dna_experiment/test_checkpoint"
#         os.mkdir(checkpoint_dir)
#         self.learner.save_checkpoint(checkpoint_dir)
#         self.assertTrue(os.path.exists(checkpoint_dir + "/model.pt"))
#         self.assertTrue(os.path.exists(checkpoint_dir + "/optimizer.pt"))
#         shutil.rmtree(checkpoint_dir)

#     def test_load_checkpoint(self):
#         checkpoint_dir = "bin/tests/test_data/dna_experiment/test_checkpoint"
#         os.mkdir(checkpoint_dir)
#         self.learner.save_checkpoint(checkpoint_dir)
#         self.learner.load_checkpoint(checkpoint_dir)
#         shutil.rmtree(checkpoint_dir)

if __name__ == "__main__":
    unittest.main()
    
    