# Kowalski
This library provides a suite of standard metrics for assessing learned feature representations, in PyTorch.

## Installation
```
pip install kowalski
```

### Example
```python
from kowalski import to_per_class_list
from kowalski.neural_collapse import class_distance_normalized_variance as cdnv
import torch
features = torch.randn(100, 128)
labels = torch.randint(0, 10, (100,))

print(cdnv(to_per_class_list(features, labels)))
```