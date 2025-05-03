import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from db import get_connection
from controllers.patient_controller import PatientController
from controllers.visit_controller import VisitController

class ViewPatientFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        self.patient_controller = PatientController()
        self.visit_controller = VisitController()
        self.controller = controller
        #create widget
        hn_label = ttk.Label(self, text = "HN")
        hn_label.pack

        hn = tk.StringVar()
        hn_entry = ttk.Entry(self, textvariable = hn)
        hn_entry.pack()

        search = ttk.Button(self, text = "search", command = lambda: self.search(hn.get()))
        search.pack()

        back = ttk.Button(self, text = "back", command = self.back)
        back.pack()

    def search(self, patient_hn):
        result = self.visit_controller.search(patient_hn)
        self.controller.set_current_patient(patient_hn)
        patient_info = self.patient_controller.view_patient(patient_hn)
        if result is not None:
            view = tk.Toplevel()
            view.geometry("500x500")
            name_label = ttk.Label(view, text = f"Name : {patient_info[1]}")
            name_label.pack(anchor="w")
            dob_label = ttk.Label(view, text = f"DOB : {patient_info[2]}")
            dob_label.pack(anchor="w")
            gender_label = ttk.Label(view, text = f"Gender : {patient_info[3]}")
            gender_label.pack(anchor="w")
            phone_label = ttk.Label(view, text = f"Phone : {patient_info[4]}")
            phone_label.pack(anchor="w")
            visit, visit_count = self.visit_controller.search(patient_hn)
            for _ in range(visit_count[0]):
                ttk.Label(view, text = f"visit {_+1}").pack()
                view_btn = ttk.Button(view, text = "view", command = lambda visit_id = visit[_][0]: self.view(visit_id))
                view_btn.pack()
            def create():
                view.destroy()
                self.controller.show_frame("CreateVisitFrame")
            create_visit = ttk.Button(view, text = "create new visit", command = create)
            create_visit.pack()
        else:
            tkinter.messagebox.showerror("Error", "404 patient not founded")
    
    def view(self, visit_id):
        #connnect to database
        conn, cursor = get_connection()
        visit_view = tk.Toplevel()
        visit_view.geometry("500x500")
        cursor.execute('''
        SELECT * FROM visit WHERE visit_id = ?
                            ''', (visit_id, ))
        visit = cursor.fetchone()
        conn.close()
        visit_date = ttk.Label(visit_view, text = f"visit date : {visit[3]}")
        visit_date.pack(anchor="w")
        visit_doctor = ttk.Label(visit_view, text = f"Doctor : {visit[1]}")
        visit_doctor.pack(anchor="w")
        visit_note = ttk.Label(visit_view, text = f"note : {visit[4]}")
        visit_note.pack(anchor="w")         

    def back(self):
        self.controller.show_frame("DashboardFrame")