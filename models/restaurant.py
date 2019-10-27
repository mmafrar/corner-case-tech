import logging
import pymysql


class RestaurantModel:
    def __init__(self):
        logging.info("Creating RestaurantModel object")
        self.connection = pymysql.connect("localhost", "admin", "admin", "food_menu_voting_app")

    def create(self, name, telephone):
        logging.info("Calling RestaurantModel.create()")
        cursor = self.connection.cursor()
        query = "INSERT INTO restaurant (name, telephone) values (%s, %s)"

        try:
            cursor.execute(query, (name, telephone))
            self.connection.commit()
            logging.info("Successfully inserted data into Restaurant table")
            return "Success!"
        except:
            self.connection.rollback()
            logging.error("Error occurred while inserting data into Restaurant table")
            return "Error!"
        finally:
            self.connection.close()
