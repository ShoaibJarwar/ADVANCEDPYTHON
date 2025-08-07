import numpy as np


np.random.seed(42)
print("Random array:", np.random.rand(3, 3))
print("Random int matrix:\n", np.random.randint(1, 10, (2, 3)))
print("Normal distribution:", np.random.normal(0, 1, 5))
# print("Normal distribution:", np.random.randn(3))
