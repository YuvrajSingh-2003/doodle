# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 21:50:09 2025
@author: lenovo
"""
a=str(input("Enter First String:"))
b=str(input("Enter Second String:"))
c=a+" "+b
print("Concatinated String:",c)
print(c.lower())
print(c.upper())
print(c.title())
print(c.capitalize())
print(c.swapcase())
print(c.strip())
old=input("Enter Old word to replace:")
new=input("Enter New word :")
print(c.replace(old, new))
sub=str(input("Enter Word to find it and its Index:"))
print(c.find(sub))
print(c.index(sub))
print(c.split("&"))
print("".join(["a","b"]))