import torch
import torch.nn as nn
from typing import Callable, Tuple, Optional

class ModelTitanic(nn.Module):
    """
    A simple model for Titanic dataset.
    """
    def __init__(self, nb_neurons_intermediate_layer: int = 7, nb_intermediate_layers: int = 3, nb_classes: int = 2):
        super(ModelTitanic, self).__init__()
        self.input_layer = nn.Linear(7, nb_neurons_intermediate_layer)
        self.intermediate = nn.modules.ModuleList([nn.Linear(nb_neurons_intermediate_layer, nb_neurons_intermediate_layer) for _ in range(nb_intermediate_layers)])
        self.output_layer = nn.Linear(nb_neurons_intermediate_layer, nb_classes)
        self.relu = nn.ReLU()
        self.softmax = nn.Softmax(dim=1)

    def forward(self, pclass: torch.Tensor, sex: torch.Tensor, age: torch.Tensor, sibsp: torch.Tensor, parch: torch.Tensor, fare: torch.Tensor, embarked: torch.Tensor) -> dict:
        """
        Forward pass of the model.
        It should return the output as a dictionary, with the same keys as `y`.

        NOTE that the final `x` is a torch.Tensor with shape (batch_size, nb_classes).
        Here nb_classes = 2, so the output is a tensor with two columns, meaning the probabilities for not survived | survived.
        """
        x = torch.stack((pclass, sex, age, sibsp, parch, fare, embarked), dim=1).float()
        x = self.relu(self.input_layer(x))
        for layer in self.intermediate:
            x = self.relu(layer(x))
        x = self.softmax(self.output_layer(x))
        return x
    
    def compute_loss(self, output: torch.Tensor, survived: torch.Tensor, loss_fn: Callable) -> torch.Tensor:
        """
        Compute the loss.
        `output` is the output tensor of the forward pass.
        `survived` is the target tensor -> label column name.
        `loss_fn` is the loss function to be used.
        """
        return loss_fn(output, survived)
    
    def batch(self, x: dict, y: dict, loss_fn: Callable, optimizer: Optional[Callable] = None) -> Tuple[torch.Tensor, dict]:
        """
        Perform one batch step.
        `x` is a dictionary with the input tensors.
        `y` is a dictionary with the target tensors.
        `loss_fn` is the loss function to be used.

        If `optimizer` is passed, it will perform the optimization step -> training step
        Otherwise, only return the forward pass output and loss -> evaluation step
        """
        output = self.forward(**x)
        loss = self.compute_loss(output, **y, loss_fn=loss_fn)
        if optimizer is not None:
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        return loss, output
