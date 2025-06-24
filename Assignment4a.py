# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 00:29:20 2025

@author: lenovo
"""

import csv
with open("address_book.csv", "w", newline='') as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Address", "Mobile", "Email"])
    writer.writerow(["Ram Praksash", "161, Ward 21, Mansarovar, Jaipur","9211420420", "ramprakash@yaahoo.com"])
    writer.writerow(["Pranay Singh", "456,parsaram Nagar, Jhotwara,Jaipur", "9874563210", "singhpran@gmail.com"])
    writer.writerow(["Michael Babu", "789 queens Road, Jaipur", "7863044201", "michael@gmail.com"])
    
with open("address_book.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)