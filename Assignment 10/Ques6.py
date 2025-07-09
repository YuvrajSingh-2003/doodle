import numpy as np
from scipy import stats

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

combined = np.concatenate((arr1, arr2), axis=0)

print("Mean:\n", np.mean(combined))
print("Median:\n", np.median(combined))
print("Mode:\n", stats.mode(combined, axis=None).mode[0])
