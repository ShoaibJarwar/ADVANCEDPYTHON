import numpy as np

data = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Sum along axis 0:", np.sum(data, axis=0)) # Col-wise
print("Sum along axis 1:", np.sum(data, axis=1)) # Row-wise
print("Mean along axis 0:", np.mean(data, axis=0))
print("Mean along axis 1:", np.mean(data, axis=1))
