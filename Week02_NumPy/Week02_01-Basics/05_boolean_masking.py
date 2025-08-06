import numpy as np

data = np.array([5, 10, 15, 20])
# mask = data < 10
# print("Mask:", mask)
# print("Filtered:", data[mask])

print("Filtered:", data[data < 12])

