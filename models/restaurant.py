import logging
from extras.database import Database


class RestaurantModel:
    def __init__(self):
        logging.info("Creating RestaurantModel object")
        self.name = None
        self.telephone = None

    def create(self):
        logging.info("Calling RestaurantModel.create()")
        database = Database()
        connection = database.get_connection()
        cursor = connection.cursor()
        query = "INSERT INTO restaurant (name, telephone) values (%s, %s)"

        try:
            cursor.execute(query, (self.name, self.telephone))
            connection.commit()
            logging.info("Successfully inserted data into Restaurant table")
            return "Success!"
        except:
            connection.rollback()
            logging.error("Error occurred while inserting data into Restaurant table")
            return "Error!"
        finally:
            connection.close()
