from models import EmployeeModel, RestaurantModel, MenuModel


class EmployeeService:
    def __init__(self):
        self.model = EmployeeModel()

    def create(self, params):
        return self.model.create(params["username"], params["email"], params["password"])


class RestaurantService:
    def __init__(self):
        self.model = RestaurantModel()

    def create(self, params):
        return self.model.create(params["name"], params["telephone"])


class MenuService:
    def __init__(self):
        self.model = MenuModel()

    def upload(self, params):
        return self.model.upload(params["item"], params["description"], params["restaurant_id"])

    def get(self):
        return self.model.get()

    def vote(self, params):
        return self.model.vote(params["menu_id"])

    def results(self):
        return self.model.results()
