# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 22:19:38 2025

@author: lenovo
"""
fact = 1
a = int(input("Enter any Number: "))
for x in range(1,a+1):
    fact = fact * x
print("Factorial is:",fact)