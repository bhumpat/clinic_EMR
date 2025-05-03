import sqlite3
from db import get_connection
import tkinter.messagebox
import datetime

class VisitModel():
    def view_visit (self, hn):
        conn, cursor = get_connection()
        try:   
            cursor.execute('''
                SELECT * FROM visit WHERE patient_hn = ?
                                ''', (hn, ))
            visit = cursor.fetchall()
            cursor.execute('''
                SELECT COUNT(visit_id) FROM visit WHERE patient_hn = ?
                                ''', (hn, ))
            visit_count = cursor.fetchone()
            return visit ,visit_count
        finally:    
            conn.close()

    def create_visit(self, doctor_name, hn, note):
        today = datetime.date.today()
        conn, cursor = get_connection()
        try :
            cursor.execute('''
                    INSERT INTO visit (users_name, patient_hn, date, note)
                    VALUES (?,?,?,?)
                    ''', (doctor_name, hn, today, note))
            conn.commit()
        except Exception as e:
            tkinter.messagebox.showerror("Error", e)
        finally:
            conn.close()