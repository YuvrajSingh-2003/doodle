# -*- coding: utf-8 -*-
"""
Created on Sat Jun 28 01:26:24 2025

@author: lenovo
"""
import pandas as pd

df = pd.read_csv("people.csv")

df_cleaned = df.drop(columns=['Index'])

df_cleaned['Date of birth'] = pd.to_datetime(df_cleaned['Date of birth'], format='%d-%m-%Y')

missing = df_cleaned.isnull().sum()
print("Missing values per column:\n", missing, "\n")

duplicates = df_cleaned.duplicated(subset='User Id').sum()
print(f"Number of duplicate User Ids: {duplicates}\n")

gender_counts = df_cleaned['Sex'].value_counts()
print("Gender distribution:\n", gender_counts, "\n")

common_jobs = df_cleaned['Job Title'].value_counts().head(5)
print("Top 5 most common job titles:\n", common_jobs, "\n")

df_cleaned.to_csv("people_cleaned.csv", index=False)
print("Cleaned data saved to people_cleaned.csv")