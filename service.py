from models import EmployeeModel, RestaurantModel


class EmployeeService:
    def __init__(self):
        self.model = EmployeeModel()

    def create(self, params):
        self.model.create(params["username"], params["email"], params["password"])


class RestaurantService:
    def __init__(self):
        self.model = RestaurantModel()

    def create(self, params):
        self.model.create(params["name"], params["telephone"])
