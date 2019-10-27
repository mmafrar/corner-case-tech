import logging
from datetime import date
from extras.database import Database


class MenuModel:
    def __init__(self):
        logging.info("Creating MenuModel object")
        self.id = None
        self.item = None
        self.description = None
        self.votes = 0
        self.restaurant_id = None
        self._date = date.today()

    def upload(self):
        logging.info("Calling MenuModel.upload()")
        database = Database()
        connection = database.get_connection()
        cursor = connection.cursor()
        query = "INSERT INTO menu (item, description, votes, restaurant_id, _date) values (%s, %s, %s, %s, %s)"

        try:
            cursor.execute(query, (self.item, self.description, self.votes, self.restaurant_id, self._date))
            connection.commit()
            logging.info("Successfully inserted data into Menu table")
            return "Success!"
        except:
            connection.rollback()
            logging.error("Error occurred while inserting data into Menu table")
            return "Error!"
        finally:
            connection.close()

    def get(self):
        logging.info("Calling MenuModel.get()")
        database = Database()
        connection = database.get_connection()
        cursor = connection.cursor()
        query = "SELECT id, item, description, restaurant_id FROM menu WHERE _date=%s"

        try:
            cursor.execute(query, (self._date,))
            logging.info("Successfully fetched data from Menu table")
            return cursor.fetchall(), cursor.description
        except:
            logging.error("Error occurred while fetching data from Menu table")
            return "Error!"
        finally:
            connection.close()

    def vote(self):
        logging.error("Calling MenuModel.vote()")
        database = Database()
        connection = database.get_connection()
        cursor = connection.cursor()
        query = "UPDATE menu set votes=votes+1 WHERE id=%s"

        try:
            cursor.execute(query, (self.id,))
            connection.commit()
            logging.info("Successfully updated the votes field in Menu table")
            return "Success!"
        except:
            connection.rollback()
            logging.error("Error occurred while updating the votes field in Menu table")
            return "Error!"
        finally:
            connection.close()

    def results(self):
        logging.info("Calling MenuModel.results()")
        database = Database()
        connection = database.get_connection()
        cursor = connection.cursor()
        query = "SELECT id, item, description, votes, restaurant_id FROM menu WHERE _date=%s"

        try:
            cursor.execute(query, (self._date,))
            logging.info("Successfully fetched data from Menu table")
            return cursor.fetchall(), cursor.description
        except:
            logging.error("Error occurred while fetching data from Menu table")
            return "Error!"
        finally:
            connection.close()
