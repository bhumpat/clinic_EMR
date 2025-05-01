import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import datetime
from db import get_connection

class CreateVisitFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        self.controller = controller

        #automatic date time
        self.today = datetime.date.today()

        #create visit frame widget
        name_label = ttk.Label(self, text = "New visit").pack(anchor="w")
        note_label = ttk.Label(self, text = "Note : ").pack(anchor="w")
        
        self.note = tk.StringVar()
        note_entry = tk.Entry(self, textvariable = self.note)
        note_entry.pack()

        submit = ttk.Button(self, text = "submit", command = self.submit)
        submit.pack(pady = 20)

        back = ttk.Button(self, text = "back", command = self.back)
        back.pack(pady = 20)

    def submit(self):
        #connnect to database
        conn, cursor = get_connection()
        cursor.execute('''
                    INSERT INTO visit (users_name, patient_hn, date, note)
                    VALUES (?,?,?,?)
                    ''', (self.user_name,
                            self.patient_hn,
                            self.today,
                            self.note.get()))
        conn.commit()
        conn.close()
        tkinter.messagebox.showinfo("approve", f"successfully add new visit")
        self.controller.show_frame("DashboardFrame")

    #get doctor name and patient id from the controller
    def set_contex(self):
        self.user_id, self.user_name = self.controller.get_current_user()
        self.patient_hn = self.controller.get_current_patient()
    def back(self):
        self.controller.show_frame("DashboardFrame")
