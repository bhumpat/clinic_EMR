import sqlite3

def get_connection():
    conn = sqlite3.connect("clinic.db")
    return conn, conn.cursor()