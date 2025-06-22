# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 21:25:20 2025

@author: lenovo
"""

a=input("Enter Student Name:")
b=input("Enter Student's Class:")
sub1=int(input("Enter Marks in English:"))
sub2=int(input("Enter Marks in Social Studies:"))
sub3=int(input("Enter Marks in Science:"))
sub4=int(input("Enter Marks in Maths:"))
sub5=int(input("Enter Marks in Hindi:"))
total= sub1+sub2+sub3+sub4+sub5
Percentage= (total/500)*100
print("Name of Student:",a)
print("Class of Student:.b")
print("Total Marks Obtained:",total)
print("Percentage Obtained:",Percentage)
if Percentage > 60:
    print("Grade:A")
elif Percentage > 50:
    print("Grade:B")
elif Percentage > 40:
    print("Grade:C")
elif Percentage > 33:
    print("Grade D")
else:
    print("Failed")