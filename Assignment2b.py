# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 12:15:14 2025

@author: lenovo
"""
items = []
total = 0
while True:
    print("\n1. Clear Bill")
    print("2. Create New Bill")
    print("3. Display Items and Prices")
    print("4. Display Total Amount")
    print("5. Exit")
    choice = int(input("Enter your choice (1-5): "))
    if choice == 1:
        items.clear()
        total = 0
        print("Bill cleared successfully")
    elif choice == 2:
        name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        items.append((name, price))
        total += price
        print(f"Added {name} - {price}")
    elif choice == 3:
        if not items:
            print("No items in bill")
        else:
            print("\nCurrent Items:")
            for name, price in items:
                print(f"{name}: {price}")
    elif choice == 4:
        print(f"\nTotal Bill Amount: {total}")
    elif choice == 5:
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter 1-5")