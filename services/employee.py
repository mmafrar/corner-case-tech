import logging
from models.employee import EmployeeModel


class EmployeeService:
    def __init__(self):
        logging.info("Creating EmployeeService object")
        self.model = EmployeeModel()

    def create(self, params):
        logging.info("Calling EmployeeService.create()")
        self.model.username = params["username"]
        self.model.email = params["email"]
        self.model.password = params["password"]
        return self.model.create()
