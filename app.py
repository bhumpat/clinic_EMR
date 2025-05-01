import tkinter as tk
from tkinter import ttk
from login import LoginFrame
from doctor_dashboard import DashboardFrame
from add_patient import AddPatientFrame
from view_patient import ViewPatientFrame
from create_visit import CreateVisitFrame

class App(tk.Tk):
    def __init__(self):
        # main app setup
        super().__init__()
        self.title("Clinic EMR")
        self.geometry("600x600")
        
        #create main frame
        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {"LoginFrame":LoginFrame(container, self),
                        "DashboardFrame":DashboardFrame(container, self),
                        "AddPatientFrame":AddPatientFrame(container, self),
                        "ViewPatientFrame":ViewPatientFrame(container, self),
                        "CreateVisitFrame":CreateVisitFrame(container,self)}
        
        for F in (LoginFrame, DashboardFrame, AddPatientFrame, ViewPatientFrame, CreateVisitFrame):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")
        #login frame
        self.show_frame(LoginFrame)

    #frame swithching method
    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()

        if hasattr(frame, "set_contex"):
            frame.set_contex()

    #recognize which doctor is using
    def set_current_user(self, doctor_id, doctor_name):
        self.current_doctor_id = doctor_id
        self.current_doctor_name = doctor_name
    
    def get_current_user(self):
        return self.current_doctor_id, self.current_doctor_name

    def set_current_patient(self, patient_hn):
        self.current_patient = patient_hn

    def get_current_patient(self):
        return self.current_patient
        
if __name__ == "__main__":
    app = App()
    app.mainloop()