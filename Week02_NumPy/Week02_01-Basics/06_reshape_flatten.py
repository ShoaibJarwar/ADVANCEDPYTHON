import numpy as np

a = np.arange(6)
reshaped = a.reshape((2, 3))
flattened = reshaped.flatten()

print("Original:\n", a)
print("Reshaped:\n", reshaped)
print("Flattened:\n", flattened)