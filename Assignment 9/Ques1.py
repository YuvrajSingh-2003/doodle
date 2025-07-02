# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 01:10:46 2025

@author: lenovo
"""

import numpy as np

array_1D = np.array([1, 2, 3])
array_2D = np.array([[4, 5], [6, 7], [8, 9]])
new_1D = array_1D[:array_2D.shape[1]].reshape(1, -1)
final_array = np.vstack((new_1D, array_2D))

print("Combined Array:\n", final_array)
