import json, logging
from datetime import date
from extras.database import Database


def convert_to_json(result, description):
    logging.info("Converting the result to JSON")
    row_headers = [x[0] for x in description]
    json_data = []
    for row in result:
        json_data.append(dict(zip(row_headers, row)))
    return json.dumps(json_data)


class MenuModel:
    def __init__(self):
        logging.info("Creating MenuModel object")
        database = Database()
        self.connection = database.get_connection()

    def upload(self, item, description, restaurant_id):
        logging.info("Calling MenuModel.upload()")
        cursor = self.connection.cursor()
        query = "INSERT INTO menu (item, description, restaurant_id, _date, votes) values (%s, %s, %s, %s, %s)"

        try:
            cursor.execute(query, (item, description, restaurant_id, date.today(), "0"))
            self.connection.commit()
            logging.info("Successfully inserted data into Menu table")
            return "Success!"
        except:
            self.connection.rollback()
            logging.error("Error occurred while inserting data into Menu table")
            return "Error!"
        finally:
            self.connection.close()

    def get(self):
        logging.info("Calling MenuModel.get()")
        cursor = self.connection.cursor()
        query = "SELECT id, item, description, restaurant_id FROM menu WHERE _date=%s"

        try:
            cursor.execute(query, (date.today(),))
            logging.info("Successfully fetched data from Menu table")
            return convert_to_json(cursor.fetchall(), cursor.description)
        except:
            logging.error("Error occurred while fetching data from Menu table")
            return "Error!"
        finally:
            self.connection.close()

    def vote(self, id):
        logging.error("Calling MenuModel.vote()")
        cursor = self.connection.cursor()
        query = "UPDATE menu set votes=votes+1 WHERE id=%s"

        try:
            cursor.execute(query, (id,))
            self.connection.commit()
            logging.info("Successfully updated the votes field in Menu table")
            return "Success!"
        except:
            self.connection.rollback()
            logging.error("Error occurred while updating the votes field in Menu table")
            return "Error!"
        finally:
            self.connection.close()

    def results(self):
        logging.info("Calling MenuModel.results()")
        cursor = self.connection.cursor()
        query = "SELECT id, item, description, votes, restaurant_id FROM menu WHERE _date=%s"

        try:
            cursor.execute(query, (date.today(),))
            logging.info("Successfully fetched data from Menu table")
            return convert_to_json(cursor.fetchall(), cursor.description)
        except:
            logging.error("Error occurred while fetching data from Menu table")
            return "Error!"
        finally:
            self.connection.close()
