# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 00:54:34 2025

@author: lenovo
"""

import pandas as pd
data_dict = {'a': 1, 'b': 2, 'c': 3}
series_dict = pd.Series(data_dict)
print("Series from Dictionary:\n",series_dict)
print("----------------------")
data_list = [10, 20, 30, 40]
series_list = pd.Series(data_list)
print("\nSeries from List:\n",series_list)
print("----------------------")
print("\nAccessing elements of Series:")
print("First element:",series_list[0])
print("Elements from index 1 to 3:\n",series_list[1:4])
print("Element with label 'b':", series_dict['b']) 