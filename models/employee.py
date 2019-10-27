import logging
from extras.database import Database


class EmployeeModel:
    def __init__(self):
        logging.info("Creating EmployeeModel object")
        self.password = None
        self.email = None
        self.username = None

    def create(self):
        logging.info("Calling EmployeeModel.create()")
        database = Database()
        connection = database.get_connection()
        cursor = connection.cursor()
        query = "INSERT INTO employee (username, email, password) values (%s, %s, %s)"

        try:
            cursor.execute(query, (self.username, self.email, self.password))
            connection.commit()
            logging.info("Successfully inserted data into Employee table")
            return "Success!"
        except:
            connection.rollback()
            logging.error("Error occurred while inserting data into Employee table")
            return "Error!"
        finally:
            connection.close()
