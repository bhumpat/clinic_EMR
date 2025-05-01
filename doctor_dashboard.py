import tkinter as tk
from tkinter import ttk

class DashboardFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        self.controller = controller
        
        #create widget 
        add_patient = ttk.Button(self, text= "Add patient", command = self.add_patient)
        add_patient.pack()
        view_patient = ttk.Button(self, text= "View patient", command = self.view_patient)
        view_patient.pack()
        logout = ttk.Button(self, text= "Logout", command = self.logout)
        logout.pack()

    def logout(self):
        self.controller.show_frame("LoginFrame")

    def add_patient(self):
        self.controller.show_frame("AddPatientFrame")

    def view_patient(self):
        self.controller.show_frame("ViewPatientFrame")
