import logging
from models import EmployeeModel, RestaurantModel, MenuModel


class EmployeeService:
    def __init__(self):
        logging.info("Creating EmployeeService object")
        self.model = EmployeeModel()

    def create(self, params):
        logging.info("Calling EmployeeService.create()")
        return self.model.create(params["username"], params["email"], params["password"])


class RestaurantService:
    def __init__(self):
        logging.info("Creating RestaurantService object")
        self.model = RestaurantModel()

    def create(self, params):
        logging.info("Calling RestaurantService.create()")
        return self.model.create(params["name"], params["telephone"])


class MenuService:
    def __init__(self):
        logging.info("Creating MenuService object")
        self.model = MenuModel()

    def upload(self, params):
        logging.info("Calling MenuService.upload()")
        return self.model.upload(params["item"], params["description"], params["restaurant_id"])

    def get(self):
        logging.info("Calling MenuService.get()")
        return self.model.get()

    def vote(self, params):
        logging.info("Calling MenuService.vote()")
        return self.model.vote(params["id"])

    def results(self):
        logging.info("Calling MenuService.results()")
        return self.model.results()
