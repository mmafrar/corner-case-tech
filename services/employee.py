import logging
from models.employee import EmployeeModel


class EmployeeService:
    def __init__(self):
        logging.info("Creating EmployeeService object")
        self.model = EmployeeModel()

    def create(self, params):
        logging.info("Calling EmployeeService.create()")
        return self.model.create(params["username"], params["email"], params["password"])
