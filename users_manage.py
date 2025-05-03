import hashlib
from db import get_connection

#connnect to database
conn, cursor = get_connection()

#Hashing password
def hash_password(password):
        h = hashlib.sha256()
        h.update(password.encode())
        hashed_password = h.hexdigest()
        return hashed_password

#Add function
def add_users():
    name = input("What's your name ? ")
    username = input("What's your username ? ")
    password = input("What's your password ? ")
    hashed_password = hash_password(password)
    role = "doctor"
    try: 
        cursor.execute('''
                   INSERT INTO users (name, username, password, role)
                   VALUES (?,?,?,?)
                   ''', (name, username, hashed_password, role))
        print(f"User '{name}' created.")
        conn.commit()
    finally:
        conn.close()

#Delete function
def delete_users():
    name = input("Which user do you want to delete ? ")
    confirm = input("Are you sure that you want to delete this user ? ")
    if confirm.lower() == "yes":
        try:
            cursor.execute('''
                       DELETE FROM users WHERE name == ?
                       ''', (name,))
            print(f"User '{name}' has been deleted")
            conn.commit()
        finally:
            conn.close()
    else:
        print("Delete canceled.")

#promt user for function
func = input("Add or Delete ? ")

if func.lower() == "add":
    add_users()
elif func.lower() == "delete":
    delete_users()
else:
     exit()