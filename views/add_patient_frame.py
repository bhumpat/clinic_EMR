import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from db import get_connection
from controllers.patient_controller import PatientController

class AddPatientFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        self.controller = controller
        self.patient_controller = PatientController()
        
        #Add patient frame widget
        name_label = ttk.Label(self, text = "Full name").pack()
        self.name = tk.StringVar()
        name_entry = ttk.Entry(self, textvariable = self.name)
        name_entry.pack()
        
        dob_label = ttk.Label(self, text = "Date of birth").pack()
        self.dob = tk.StringVar()
        dob_entry = ttk.Entry(self, textvariable = self.dob)
        dob_entry.pack()
        
        gender_label = ttk.Label(self, text = "Gender").pack()
        self.gender = tk.StringVar()
        gender_entry = ttk.Entry(self, textvariable = self.gender)
        gender_entry.pack()
        
        number_label = ttk.Label(self, text = "Phone number").pack()
        self.phone = tk.StringVar()
        phone_entry = ttk.Entry(self, textvariable = self.phone)
        phone_entry.pack()
        
        submit = ttk.Button(self, text = "submit", command = self.submit)
        submit.pack(pady = 20)
        
        back = ttk.Button(self, text = "back", command = self.back)
        back.pack(pady = 20)

    def submit(self):
        try:
            self.patient_controller.add_patient(
                self.name.get(),
                self.dob.get(),
                self.gender.get(),
                self.phone.get()
                )
            tkinter.messagebox.showinfo("success", f"Added '{self.name.get()}'")
            self.name.set("")
            self.dob.set("")
            self.gender.set("")
            self.phone.set("")
        except Exception as e:
            tkinter.messagebox.showerror("Error", e)
    
    def back(self):
        self.controller.show_frame("DashboardFrame")
