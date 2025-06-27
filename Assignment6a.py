# -*- coding: utf-8 -*-
"""
Created on Sat Jun 28 00:20:45 2025

@author: lenovo
"""

import pandas as pd
date=["25-06-2025","26-06-2025","27-06-2025","28-06-2025"]
values=[100,50,25,10]
df=pd.DataFrame({"date":date,
                "value":values})
df["date"]=pd.to_datetime(df["date"],format="%d-%m-%Y")
df.set_index("date",inplace=True)
print(df)