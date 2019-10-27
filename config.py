import logging


class ApplicationConfig:
    LOG_FILENAME = "app.log"
    LOG_LEVEL = logging.DEBUG
    LOG_FORMAT = "%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s"
    PROJECT_ROOT = "/home/mmafrar/Documents/food-menu-voting-app/"


class DatabaseConfig:
    DB_HOST = "localhost"
    DB_USERNAME = "admin"
    DB_PASSWORD = "admin"
    DB_NAME = "food_menu_voting_app"
