import logging
import pymysql
from config import ApplicationConfig, DatabaseConfig


class Database:
    def __init__(self):
        logging.info("Creating Database object")
        self.host = DatabaseConfig.DB_HOST
        self.username = DatabaseConfig.DB_USERNAME
        self.password = DatabaseConfig.DB_PASSWORD
        self.database = DatabaseConfig.DB_NAME

    def get_connection(self):
        connection = None
        try:
            connection = pymysql.connect(self.host, self.username, self.password, self.database)
            logging.info("Database connection created")
        except:
            logging.error("Error connecting to the database")
        logging.info("Returning database connection")
        return connection

    def recreate_tables(self):
        logging.info("Calling Database.recreate_tables()")
        connection = self.get_connection()
        cursor = connection.cursor()
        file = open(ApplicationConfig.PROJECT_ROOT + "database.sql", "r")
        query = file.read().replace("\n", "").strip().split(";")
        query.pop()

        try:
            for line in query:
                cursor.execute(line)
            connection.commit()
            logging.info("Database tables successfully recreated")
            return "Success!"
        except:
            connection.rollback()
            logging.error("Error occurred while recreating database tables")
            return "Error!"
        finally:
            file.close()
            connection.close()
