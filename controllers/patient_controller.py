from models.patient_model import PatientModel

class PatientController():
    def __init__(self,):
        self.model = PatientModel()
    
    def add_patient(self, name, dob, gender, phone):
        self.model.add_patient(name, dob, gender, phone)

    def view_patient(self, hn):
        return self.model.view_patient(hn)
        
