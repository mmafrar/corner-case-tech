import logging
import pymysql
from config import DatabaseConfig


class Database:
    def __init__(self):
        logging.info("Creating Database object")
        self.host = DatabaseConfig.HOST
        self.username = DatabaseConfig.USERNAME
        self.password = DatabaseConfig.PASSWORD
        self.database = DatabaseConfig.DATABASE

    def get_connection(self):
        connection = None
        try:
            connection = pymysql.connect(self.host, self.username, self.password, self.database)
            logging.info("Database connection created")
        except:
            logging.error("Error connecting to the database")
        logging.info("Returning database connection")
        return connection
