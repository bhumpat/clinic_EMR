import sqlite3
from db import get_connection
import tkinter.messagebox

class PatientModel():
    def add_patient(self, name, dob, gender, phone):
        conn, cursor = get_connection()
        try:
            cursor.execute('''
                    INSERT INTO patient (name, dob, gender, phone)
                    VALUES (?,?,?,?)
                    ''', (name, dob, gender, phone))
            conn.commit()
        finally:
            conn.close()
    
    def view_patient(self, hn):
        try:
            conn, cursor = get_connection()
            cursor.execute('''
            SELECT * FROM patient WHERE hn = ?
                        ''', (hn, ))
            return cursor.fetchone()
        finally:
            conn.close()
    

    