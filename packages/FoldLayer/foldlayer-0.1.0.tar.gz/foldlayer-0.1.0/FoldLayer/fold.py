import torch                    # type: ignore
import torch.nn as nn           # type: ignore
import torch.nn.functional as F # type: ignore




###################################### Fold Module ######################################


class Fold(nn.Module):
    """
    A PyTorch module that performs a folding operation on input tensors along a specified direction.
    """
    def __init__(self, width:int, leak:float=0, 
                 fold_in:bool=True, has_stretch:bool=False, track_importance:bool=False) -> None:
        """
        Thus function initializes the Fold module.
        Parameters:
            width (int): The expected input dimension.
            leak (float, optional): The leak parameter for the fold operation.
            fold_in (bool): Whether to fold in or fold out.
            has_stretch (bool): Whether the module allows stretching.
            track_importance (bool): Whether to track how important the fold is.
        """
        super().__init__()
        # Hyperparameters
        self.width = width
        self.leak = leak
        self.fold_in = fold_in
        self.has_stretch = has_stretch
        self.track_importance = track_importance
        self.importance = 0
        
        # Parameters
        min_norm = 1e-2
        n = torch.randn(self.width) * (2 / self.width) ** 0.5
        while n.norm().item() < min_norm:
            n = torch.randn(self.width) * (2 / self.width) ** 0.5
        self.n = nn.Parameter(n)
            
        # Initialize stretch as a parameter if needed
        no_stretch = torch.tensor(2.0)
        if self.has_stretch:
            self.stretch = nn.Parameter(no_stretch)
        else:
            self.register_buffer('stretch', no_stretch)
    
    
    def forward(self, input:torch.Tensor) -> torch.Tensor:
        """
        This function performs the folding operation on the input tensor.
        Parameters:
            input (torch.Tensor): The input tensor of shape (batch_size, input_dim).
        Returns:
            folded (torch.Tensor): The transformed tensor after the folding operation.
        """
        # pad the input if the width is greater than the input width, raise error if input width is greater than fold width
        if self.width > input.shape[1]:
            input = F.pad(input, (0, self.width - input.shape[1]))
        elif self.width < input.shape[1]:
            raise ValueError(f"Input dimension ({input.shape[1]}) is greater than fold width ({self.width})")

        # Compute scales
        eps = 1e-8
        scales = (input @ self.n) / (self.n @ self.n + eps)
        
        # If it is a fold in, we want to fold in the values that are greater than 1
        if self.fold_in:
            indicator = (scales > 1).float()
        else:
            indicator = (scales < 1).float()
        if self.track_importance:
            self.importance = indicator.mean().item()
        indicator = indicator + (1 - indicator) * self.leak

        # Compute the projected and folded values
        projection = scales.unsqueeze(1) * self.n
        folded = input + self.stretch * indicator.unsqueeze(1) * (self.n - projection)
        return folded