import numpy as np
arr3d = np.random.rand(2, 3, 4)  
moved = np.moveaxis(arr3d, 0, -1)  
print("New shape:", moved.shape)