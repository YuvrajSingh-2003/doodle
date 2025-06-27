# -*- coding: utf-8 -*-
"""
Created on Sat Jun 28 01:08:15 2025

@author: lenovo
"""

import pandas as pd
df1 = pd.DataFrame({
    "ID":[1,2,3,4,5],
    "Name":["Raj","Dev","Arjun","Karan","Kali"],
    "Car":["Ford","Hyundai","Suzuki","Mercedes","BMW"]})

df2 = pd.DataFrame({
    "ID":[3,4,5,6,7],
    "Car_Price":[50000,30000,40000,100000,80000],
    "Years_used":["3_Years","2_Years","5_Years","1_Year","4_Years"]})

df3 = pd.DataFrame({
    'ID': [1, 2, 2, 3],
    'Project': ['A', 'B', 'C', 'A'],
    'Hours': [40, 30, 20, 35]})

Inner_Merge=pd.merge(df1, df2,on="ID")#inner merge
print("\nInner merge:")
print(Inner_Merge)

left_Mer=pd.merge(df1, df2,on="ID",how="left")
print("\nLeft merge of Dataframes:")
print(left_Mer)

Right_Mer=pd.merge(df1, df2,on="ID",how="right")
print("\nRight merge of Dataframes:")
print(Right_Mer)

df1_indexed = df1.set_index("ID")
df2_indexed = df2.set_index("ID")
index_joined = df1_indexed.join(df2_indexed, how="right")
print("\nIndex-Based Join (df.join) with Right Join:")
print(index_joined)

multi_merged = pd.merge(Inner_Merge, df3,on="ID")
print("\nMerge with multiple matching keys:")
print(multi_merged)
