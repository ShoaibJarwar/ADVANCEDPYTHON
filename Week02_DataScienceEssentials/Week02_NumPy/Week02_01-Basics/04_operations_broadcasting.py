import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Addition:", a + b)
print("Multiplication:", a * b)
print("Power:", a ** 2)

# Broadcasting
a = np.array([
    [1],
    [2],
    [3]
])
b = np.array([1, 2, 3])
print("Broadcasting Result:\n", a + b)
