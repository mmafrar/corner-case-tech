import logging
from extras.utilities import Utilities
from models.menu import MenuModel


class MenuService:
    def __init__(self):
        logging.info("Creating MenuService object")
        self.model = MenuModel()

    # Calls the method from MenuModel with a Menu object
    def upload(self, params):
        logging.info("Calling MenuService.upload()")
        self.model.item = params["item"]
        self.model.description = params["description"]
        self.model.restaurant_id = params["restaurant_id"]
        return self.model.upload()

    # Get query results from MenuModel and return it after converting to JSON
    def get(self):
        logging.info("Calling MenuService.get()")
        result = self.model.get()
        return Utilities.convert_to_json(result[0], result[1])

    # Calls MenuModel after voted with a Menu object with id
    def vote(self, params):
        logging.info("Calling MenuService.vote()")
        self.model.id = params["id"]
        return self.model.vote()

    # Get Menu results for the day and return it after converting to JSON
    def results(self):
        logging.info("Calling MenuService.results()")
        result = self.model.results()
        return Utilities.convert_to_json(result[0], result[1])
