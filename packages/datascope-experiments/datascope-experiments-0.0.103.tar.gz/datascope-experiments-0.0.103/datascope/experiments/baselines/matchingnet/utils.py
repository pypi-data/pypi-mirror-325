import torch
from torch import Tensor


def compute_prototypes(support_features: Tensor, support_labels: Tensor) -> Tensor:
    """
    Compute class prototypes from support features and labels
    Args:
        support_features: for each instance in the support set, its feature vector
        support_labels: for each instance in the support set, its label

    Returns:
        for each label of the support set, the average feature vector of instances with this label
    """

    n_way = len(torch.unique(support_labels))
    # Prototype i is the mean of all instances of features corresponding to labels == i
    return torch.cat([support_features[torch.nonzero(support_labels == label)].mean(0) for label in range(n_way)])
