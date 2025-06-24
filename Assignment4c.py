# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 01:17:59 2025

@author: lenovo
"""

import sqlite3

conn = sqlite3.connect("assignmentdb.db")
conn.execute("""
    CREATE TABLE users (
        userid INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(100),
        pass VARCHAR(50),
        mobile VARCHAR(50),
        email VARCHAR(50))
        """)
conn.execute("""
    CREATE TABLE products (
        productid INTEGER PRIMARY KEY AUTOINCREMENT,
        productname VARCHAR(100),
        price REAL,
        stock INTEGER)
        """)
conn.close()

# Insert records
conn = sqlite3.connect("assignmentdb.db")
conn.execute("""
    INSERT INTO users (username, pass, mobile, email)
    VALUES ("dkon", "hellu", "9012365478", "dkon420@gmail.com")
    """)
conn.execute("""
    INSERT INTO users (username, pass, mobile, email)
    VALUES ("akona", "password", "9573654321", "akona11@gmail.com")
    """)
conn.execute("""
    INSERT INTO users (username, pass, mobile, email)
    VALUES ("bobby", "bob123", "9211786420", "bobbi99@gmail..com")
    """)
conn.execute("""
    INSERT INTO products (productname, price, stock)
    VALUES ("Laptop", 1000, 10)
""")
conn.execute("""
    INSERT INTO products (productname, price, stock)
    VALUES ("Smartphone", 500, 15)
""")
conn.commit()
conn.close()

# print records
print("Users:")
conn = sqlite3.connect("assignmentdb.db")
users = conn.execute("SELECT * FROM users")
for user in users:
    print(user)
conn.close()

print("\nProducts:")
conn = sqlite3.connect("assignmentdb.db")
products = conn.execute("SELECT * FROM products")
for product in products:
    print(product)
conn.close()

# update
conn = sqlite3.connect("assignmentdb.db")
conn.execute("""
    UPDATE users
    SET username = "dobby"
    WHERE userid = 1
""")
conn.commit()
conn.close()

print("\nAfter Update:")
conn = sqlite3.connect("assignmentdb.db")
users = conn.execute("SELECT * FROM users")
for user in users:
    print(user)
conn.close()

# Delete
conn = sqlite3.connect("assignmentdb.db")
conn.execute("DELETE FROM users WHERE userid = 2")
conn.commit()
conn.close()

print("\nAfter deletion:")
conn = sqlite3.connect("assignmentdb.db")
users = conn.execute("SELECT * FROM users")
for user in users:
    print(user)
conn.close()
