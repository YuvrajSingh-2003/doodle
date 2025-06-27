# -*- coding: utf-8 -*-
"""
Created on Sat Jun 28 01:26:22 2025

@author: lenovo
"""

import pandas as pd
#date-time objects
date = "2025-06-28"
date_ob = pd.to_datetime(date)
print("\n Created a date time object",date_ob)

#Date Range
date_range = pd.date_range(start="2025-06-15",end="2025-06-25")
print("\nGenerated Range:")
print(date_range)

#Filtering 
data = {
        "date":pd.date_range(start="2025-06-15",end="2025-06-20"),
        "Values":[5,4,9,3,10,2]}
df1 = pd.DataFrame(data)
fil_df = df1[df1["date"]>"2025-06-17"]
print("\nFiltered Dates:\n")
print(fil_df)

# Extracting
df2 = pd.DataFrame({'date': pd.to_datetime(['2023-01-01', '2023-02-15', '2023-03-20'])})
df2['year'] = df2['date'].dt.year
df2['month'] = df2['date'].dt.month
df2['day'] = df2['date'].dt.day
print("Extracted Date Components:")
print(df2)