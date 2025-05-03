from models.visit_model import VisitModel

class VisitController():
    def __init__(self,):
        self.model = VisitModel()

    def search(self, hn):
        return self.model.view_visit(hn)
    
    def create_visit(self, doctor_name, hn, note):
        self.model.create_visit(doctor_name, hn, note)