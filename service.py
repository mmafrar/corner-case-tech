from models import EmployeeModel


class EmployeeService:
    def __init__(self):
        self.model = EmployeeModel()

    def create(self, params):
        self.model.create(params["username"], params["email"], params["password"])
