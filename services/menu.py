import logging
from models.menu import MenuModel


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
