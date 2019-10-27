import logging
from extras.database import Database


class EmployeeModel:
    def __init__(self):
        logging.info("Creating EmployeeModel object")
        database = Database()
        self.connection = database.get_connection()

    def create(self, username, email, password):
        logging.info("Calling EmployeeModel.create()")
        cursor = self.connection.cursor()
        query = "INSERT INTO employee (username, email, password) values (%s, %s, %s)"

        try:
            cursor.execute(query, (username, email, password))
            self.connection.commit()
            logging.info("Successfully inserted data into Employee table")
            return "Success!"
        except:
            self.connection.rollback()
            logging.error("Error occurred while inserting data into Employee table")
            return "Error!"
        finally:
            self.connection.close()
