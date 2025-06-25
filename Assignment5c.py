# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 00:13:00 2025

@author: lenovo
"""

import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]})

print("Original DataFrame:")
print(df)

# iloc (integer)
print("Iterate using iloc:")
for i in range(len(df)):
    row = df.iloc[i]
    print(f"Index: {i}, A: {row['A']}, B: {row['B']}")
print("\n")

# loc (label ) -
print("Iterate using loc:")
for i in df.index:
    row = df.loc[i]
    print(f"Index: {i}, A: {row['A']}, B: {row['B']}")
print("\n")

# Select row
print("Select first row using iloc[0]:")
print(df.iloc[0])
print("\n")

# row selection within column
print("First two rows of column 'A':")
print(df.loc[:1, 'A'])
print("\n")

# Drop rows
print("DataFrame after dropping rows where A < 3:")
df_drop = df[df['A'] >= 3].reset_index(drop=True)
print(df_drop)
print("\n")

# Insert row
print("Insert row {'A':4, 'B':7} at index 1:")
new_row = {'A': 4, 'B': 7}
new_df = pd.DataFrame([new_row])
insert = pd.concat([df_drop.iloc[:1], new_df, df_drop.iloc[1:]]).reset_index(drop=True)
print(insert)

# Create a list
print("List of values in column 'A':")
list = insert['A'].tolist()
print(list)

