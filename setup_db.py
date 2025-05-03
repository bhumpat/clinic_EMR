from db import get_connection

#connnect to database
conn, cursor = get_connection()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               username TEXT,
               password TEXT,
               name TEXT,
               role TEXT)
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS patient(
               hn INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               dob DATETIME,
               gender TEXT,
               phone TEXT)         
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS visit(
               visit_id INTEGER PRIMARY KEY AUTOINCREMENT,
               users_name text,
               patient_hn INTEGER,
               date DATETIME,
               note TEXT,
               FOREIGN KEY (users_name) REFERENCES users(name),
               FOREIGN KEY (patient_hn) REFERENCES patient(hn)) 
''')

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print("Tables created:", tables)

conn.commit()
conn.close()