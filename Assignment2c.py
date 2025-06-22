# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 22:32:01 2025

@author: lenovo
"""

a = input("Enter elements sepearated by Spaces(Preferabely Int type): ")
list = a.split()
print("List:", list)
b = max(list)
print("Maximum Element of List:",b)
list.remove(b)
c = max(list)
print("Second max element of list:",c)
d = min(list)
list.remove(d)
e = min(list)
print("Second minimum element of list:",e)