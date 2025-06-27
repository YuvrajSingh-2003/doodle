# -*- coding: utf-8 -*-
"""
Created on Sat Jun 28 00:52:19 2025

@author: lenovo
"""

import pandas as pd
df1 = pd.DataFrame({
    "ID":[1,2,3],
    "Name":["Raj","Dev","Arjun"],
    "Car":["Ford","Hyundai","Suzuki"]})
df2 = pd.DataFrame({
    "ID":[4,5],
    "Name":["Karan","Kali"],
    "Car":["Mercedes","BMW"]})
df3 = pd.DataFrame({
    "ID":[1,2,3,4,5],
    "Car_Price":[50000,30000,40000,100000,80000],
    "Years_used":["3_Years","2_Years","5_Years","1_Year","4_Years"]})
#vertically Concatinate
Con_df=pd.concat([df1,df2])
print("\nConcatenated Dataframe:\n")
print(Con_df)

#merged horizontally
Mer_df=pd.merge(Con_df, df3,on="ID")
print("\nMerged Dataframe:")
print(Mer_df)
"""
df.join()
1.Joins DataFrames based on their indexes.
2.Performs a left join by default.
3.Less Flexible
4.Best for quickly combining DataFrames aligned by index.

pd.merge()
1.Merges DataFrames based on one or more columns (not just indexes).
2.Performs an inner join by default.
3.More flexible; allows specifying keys and join types (inner, outer, left, right).
4.Ideal for complex merging scenarios with non-index keys.
"""