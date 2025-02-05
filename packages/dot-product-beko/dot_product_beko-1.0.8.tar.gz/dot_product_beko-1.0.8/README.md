# dot_product

Fast dot product computation using Assembly (AVX2). 

## Installation

```pip install dot-product-beko```

## Usage

```python
import numpy as np
from dot_product import dot_product

x = np.random.rand(1000000).astype(np.float64)
y = np.random.rand(1000000).astype(np.float64)

result = dot_product(x, y)
print("Dot Product:", result)
```