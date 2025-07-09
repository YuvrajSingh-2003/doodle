import numpy as np
arr = np.array([[1, np.nan, 3], [4, 5, np.nan], [7, 8, 9]])
col_mean = np.nanmean(arr, axis=0)
inds = np.where(np.isnan(arr))
arr[inds] = np.take(col_mean, inds[1])
print("Array with NaNs replaced by column averages:\n", arr)