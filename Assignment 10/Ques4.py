import numpy as np
arr = np.array([[1, -2, 3], [-4, 5, -6]])
arr = np.where(arr < 0, 0, arr)
print("Negative values replaced with 0:\n", arr)