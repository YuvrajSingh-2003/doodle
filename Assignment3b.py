# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 00:59:27 2025

@author: lenovo
"""

def is_palindrome(number):
    return str(number) == str(number)[::-1]
num = int(input("Enter a number to check for palindrome: "))
if is_palindrome(num):
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")