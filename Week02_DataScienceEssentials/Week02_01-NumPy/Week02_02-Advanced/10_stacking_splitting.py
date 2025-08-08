import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Horizontal stacking:\n", np.hstack((a, b)))
print("Vertical stacking:\n", np.vstack((a, b)))


arr = np.array([
    [1, 2, 3, 8],
    [4, 5, 6, 7]
])
print("Split into 4 columns:", np.hsplit(arr, 4))
"""[
    array([[1], [4]]), 
    array([[2], [5]]), 
    array([[3], [6]]), 
    array([[8], [7]])
]"""


"""
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Stacking
print("Vertical Stack:\n", np.vstack((a, b)))
print("Horizontal Stack:\n", np.hstack((a, b)))

# Splitting
c = np.array([[1, 2, 3], [4, 5, 6]])
print("Split horizontally:\n", np.hsplit(c, 3))
print("Split vertically:\n", np.vsplit(c, 2))

"""