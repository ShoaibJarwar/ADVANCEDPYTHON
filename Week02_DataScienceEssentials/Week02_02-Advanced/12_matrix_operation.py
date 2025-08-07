import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Dot Product:\n", np.dot(A, B))
print("Transpose:\n", A.T)
print("Inverse:\n", np.linalg.inv(A))
