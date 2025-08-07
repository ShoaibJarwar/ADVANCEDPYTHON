import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print("Single Index:", arr[0])
print("Slice:", arr[1:4])

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Index:", matrix[1, 2])
print("Column slice:", matrix[:, 1])
