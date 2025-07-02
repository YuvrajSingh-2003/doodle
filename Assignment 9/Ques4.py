# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 01:23:52 2025

@author: lenovo
"""
import numpy as np
array = np.array([[1, 2, 3], [4, 5, 6]])

max_value = np.max(array)
min_value = np.min(array)

num_rows, num_cols = array.shape

elements = array.flatten()
specific_element = array[1, 2]

Sum = 0
for row in array:
    Sum += np.sum(row)

array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[7, 8, 9], [10, 11, 12]])
add = array1 + array2
sub = array1 - array2
mul = array1 * array2
div = array1 / array2

# Print results
print("Maximum Value:", max_value)
print("Minimum Value:", min_value)
print("Number of Rows:", num_rows)
print("Number of Columns:", num_cols)
print("All Elements:\n",elements)
print("Specific Element (row 1, col 2):", specific_element)
print("Sum of Values in 2D Array:", Sum)
print("Added Arrays:\n", add)
print("Subtracted Arrays:\n", sub)
print("Multiplied Arrays:\n", mul)
print("Divided Arrays:\n", div)
