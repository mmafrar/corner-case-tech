import logging
from models.restaurant import RestaurantModel


class RestaurantService:
    def __init__(self):
        logging.info("Creating RestaurantService object")
        self.model = RestaurantModel()

    def create(self, params):
        logging.info("Calling RestaurantService.create()")
        return self.model.create(params["name"], params["telephone"])
