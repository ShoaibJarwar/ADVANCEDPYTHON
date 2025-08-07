import numpy as np

arr = np.array([1, 3, 5, 7, 9, 11])
np.save('my_array.npy', arr)

loaded = np.load('my_array.npy')
print("Loaded Array:", loaded)