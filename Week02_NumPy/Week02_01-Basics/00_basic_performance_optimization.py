import numpy as np
import time

size = 1_000_000
list1 = list(range(size))
# list1 = [1,2,3,4]
list2 = list(range(size))
# list2 = [5,6,7,8]

start = time.time()
result = [x + y for x, y in zip(list1, list2)]

print("List addition time:", time.time() - start) 
# print(result)
arr1 = np.arange(size)
arr2 = np.arange(size)

start = time.time()
result = arr1 + arr2
print("NumPy addition time:", time.time() - start)
