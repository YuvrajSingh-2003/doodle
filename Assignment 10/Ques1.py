import numpy as np
arr = np.array([[6, -8, 73, -110], [np.nan, -8, 0, 94]])
arr = np.nan_to_num(arr)
arr_3x3 = arr[:2, :3]  
arr_3x3_swapped = arr_3x3.T
print("Modified array:\n", arr_3x3_swapped)