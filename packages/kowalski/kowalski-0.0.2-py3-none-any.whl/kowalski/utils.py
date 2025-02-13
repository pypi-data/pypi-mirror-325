from jaxtyping import Integer, Shaped
from torch import Tensor


def to_per_class_list(
    features: Shaped[Tensor, 'batch *axes'], labels: Integer[Tensor, 'batch']
) -> list[Shaped[Tensor, 'batch dim']]:
    """
    Converts a batch of features and their labels to a list of per-class features.

    Parameters
    ----------
    features: Batched tensor.
    labels: Batched integer labels.

    Returns
    -------
    A list of per-class features, sorted by class label.
    """
    unique_labels = labels.unique(sorted=True)
    return [features[labels == label] for label in unique_labels]
