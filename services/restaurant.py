import logging
from models.restaurant import RestaurantModel


class RestaurantService:
    def __init__(self):
        logging.info("Creating RestaurantService object")
        self.model = RestaurantModel()

    # Calls the method from RestaurantModel with a Restaurant object
    def create(self, params):
        logging.info("Calling RestaurantService.create()")
        self.model.name = params["name"]
        self.model.telephone = params["telephone"]
        return self.model.create()
