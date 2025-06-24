# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 00:59:41 2025

@author: lenovo
"""

import pandas as pd

# Pandas DataFrame using 2D list
data_2d = [[1, 'Akon'], [2, 'Bkon'], [3, 'Ckon']]
df_2d = pd.DataFrame(data_2d, columns=['ID', 'Name'])
print("DataFrame from 2D List:")
print(df_2d)

# DataFrame from dict
data_dict = {
    'ID': [1, 2, 3],
    'Name': ['Alex', 'Bobby', 'Chuck']
}
df_dict = pd.DataFrame(data_dict)
print("\nDataFrame from Dictionary:")
print(df_dict)

# DataFrame using list of lists
listoflists = [['Akon', 24], ['Bkon', 30], ['Ckon', 22]]
df_listoflists = pd.DataFrame(listoflists, columns=['Name', 'Age'])
print("\nDataFrame from List of Lists:")
print(df_listoflists)

# DataFrame using List of tuples
listoftuples = [('Alex', 24), ('Bobby', 30), ('Chuck', 22)]
df_listoftuples = pd.DataFrame(listoftuples, columns=['Name', 'Age'])
print("\nDataFrame from List of Tuples:")
print(df_listoftuples)

# DataFrame from List of dicts
listofdicts = [
               {'Name': 'Akon', 'Age': 24},
               {'Name': 'Bkon', 'Age': 30},
               {'Name': 'Ckon', 'Age': 22}
               ]
df_listofdicts = pd.DataFrame(listofdicts)
print("\nDataFrame from List of Dicts:")
print(df_listofdicts)