import sqlite3
import hashlib
import getpass


def initialize_database():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS Users(
            username VARCHAR PRIMARY KEY,
            password VARCHAR,
            logged_in INT NOT NULL DEFAULT 0)
        ''')
    connection.commit()
    connection.close()


def secure_password(password):
    temp = password.encode()
    secured = hashlib.sha256(temp)
    secured_password = secured.hexdigest()
    return secured_password


def register():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    while True:
        username = input("Enter username: ").strip()
        if username == "":
            print("Username cannot be empty, try again.")
        elif " " in username:
            print("Username cannot contain spaces, try again.")
        else:
            break

    # Case-insensitive check for username existence
    cursor.execute(f"SELECT username FROM Users WHERE LOWER(username) = LOWER('{username}')")
    user_exists = False
    for row in cursor:
        user_exists = True
        break
    if user_exists:
        print("Username already exists.")
        connection.close()
        return
    else:
        print("Username is available.")

    while True:
        password = getpass.getpass("Enter password: ")
        confirm_password = getpass.getpass("Confirm password: ")
        if password != confirm_password:
            print("Passwords do not match, try again.")
        elif password == "":
            print("Password cannot be empty, try again.")
        elif " " in password:
            print("Password cannot contain spaces, try again.")
        else:
            break

    hashed_password = secure_password(password)
    cursor.execute(f"INSERT INTO Users (username, password, logged_in) VALUES ('{username}', '{hashed_password}', 0)")
    connection.commit()
    connection.close()
    print(f"User '{username}' successfully registered.")


def login(current):
    if current is not None:
        print("Already logged in, please logout first.")
        return current

    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    username = input("Enter username: ").strip()
    password = getpass.getpass("Enter password: ")
    hashed_password = secure_password(password)

    # Case-insensitive username match
    cursor.execute(f"SELECT password, logged_in FROM Users WHERE LOWER(username) = LOWER('{username}')")
    stored_password = None
    logged_in = 0
    found = False
    for row in cursor:
        stored_password = row[0]
        logged_in = row[1]
        found = True
        break
    if not found:
        print("User does not exist")
        connection.close()
        return None
    if logged_in == 1:
        print("User already logged in")
        connection.close()
        return None
    if hashed_password == stored_password:
        # Set logged_in=1 for that username (case-insensitive update)
        cursor.execute(f"UPDATE Users SET logged_in = 1 WHERE LOWER(username) = LOWER('{username}')")
        connection.commit()
        connection.close()
        print(f"{username} is now logged in")
        return username
    else:
        print("Incorrect password")
        connection.close()
        return None


def logout(current):
    if current is None:
        print("No user is currently logged in.")
        return None
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute(f"UPDATE Users SET logged_in = 0 WHERE LOWER(username) = LOWER('{current}')")
    connection.commit()
    connection.close()
    print(f"User '{current}' logged out successfully.")
    return None


def change_password(current):
    if current is None:
        print("You must be logged in to change your password.")
        return

    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    current_password = getpass.getpass("Enter current password: ")
    hashed_current_password = secure_password(current_password)

    cursor.execute(f"SELECT password FROM Users WHERE LOWER(username) = LOWER('{current}')")
    stored_password = None
    for row in cursor:
        stored_password = row[0]
        break

    if hashed_current_password != stored_password:
        print("Current password is incorrect.")
        connection.close()
        return

    while True:
        new_password = getpass.getpass("Enter new password: ")
        new_password_confirm = getpass.getpass("Confirm new password: ")
        if new_password != new_password_confirm:
            print("Passwords do not match, try again.")
        elif new_password == "":
            print("Password cannot be empty, try again.")
        elif " " in new_password:
            print("Password cannot contain spaces, try again.")
        else:
            break

    hashed_new_password = secure_password(new_password)
    cursor.execute(f"UPDATE Users SET password = '{hashed_new_password}' WHERE LOWER(username) = LOWER('{current}')")
    connection.commit()
    connection.close()
    print("Password changed successfully.")


def main():
    initialize_database()
    current_user = None

    while True:
        print("\nUser Management System")
        print("1. Register")
        print("2. Login")
        print("3. Logout")
        print("4. Change Password")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            register()
        elif choice == "2":
            current_user = login(current_user)
        elif choice == "3":
            current_user = logout(current_user)
        elif choice == "4":
            change_password(current_user)
        elif choice == "5":
            if current_user:
                current_user = logout(current_user)
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


main()