# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 01:32:04 2025

@author: lenovo
"""
def calculator():
    print("\nBasic Calculator")
    print("Operations available: + (add), - (subtract), * (multiply), / (divide), % (modulo)")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /, %): ")
        
    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    elif operation == '%':
        result = num1 % num2
        print(f"{num1} % {num2} = {result}")
    else:
        print("Invalid operation selected")
    
calculator()