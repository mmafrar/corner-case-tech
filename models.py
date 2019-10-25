import json, pymysql
from datetime import date


def convert_to_json(result, description):
    row_headers = [x[0] for x in description]
    json_data = []
    for row in result:
        json_data.append(dict(zip(row_headers, row)))
    return json.dumps(json_data)


class EmployeeModel:
    def __init__(self):
        self.connection = pymysql.connect("localhost", "admin", "admin", "food_menu_voting_app")

    def create(self, username, email, password):
        cursor = self.connection.cursor()
        query = "INSERT INTO employee (username, email, password) values (%s, %s, %s)"

        try:
            cursor.execute(query, (username, email, password))
            self.connection.commit()
            return "Success!"
        except:
            self.connection.rollback()
            return "Error!"
        finally:
            self.connection.close()


class RestaurantModel:
    def __init__(self):
        self.connection = pymysql.connect("localhost", "admin", "admin", "food_menu_voting_app")

    def create(self, name, telephone):
        cursor = self.connection.cursor()
        query = "INSERT INTO restaurant (name, telephone) values (%s, %s)"

        try:
            cursor.execute(query, (name, telephone))
            self.connection.commit()
            return "Success!"
        except:
            self.connection.rollback()
            return "Error!"
        finally:
            self.connection.close()


class MenuModel:
    def __init__(self):
        self.connection = pymysql.connect("localhost", "admin", "admin", "food_menu_voting_app")

    def upload(self, item, description, restaurant_id):
        cursor = self.connection.cursor()
        query = "INSERT INTO menu (item, description, restaurant_id, _date, votes) values (%s, %s, %s, %s, %s)"

        try:
            cursor.execute(query, (item, description, restaurant_id, date.today(), "0"))
            self.connection.commit()
            return "Success!"
        except:
            self.connection.rollback()
            return "Error!"
        finally:
            self.connection.close()

    def get(self):
        cursor = self.connection.cursor()
        query = "SELECT id, item, description, restaurant_id FROM menu WHERE _date=%s"

        try:
            cursor.execute(query, (date.today(),))
            return convert_to_json(cursor.fetchall(), cursor.description)
        except:
            return "Error!"
        finally:
            self.connection.close()

    def vote(self, id):
        cursor = self.connection.cursor()
        query = "UPDATE menu set votes=votes+1 WHERE id=%s"

        try:
            cursor.execute(query, (id,))
            self.connection.commit()
            return "Success!"
        except:
            self.connection.rollback()
            return "Error!"
        finally:
            self.connection.close()

    def results(self):
        cursor = self.connection.cursor()
        query = "SELECT id, item, description, votes, restaurant_id FROM menu WHERE _date=%s"

        try:
            cursor.execute(query, (date.today(),))
            return convert_to_json(cursor.fetchall(), cursor.description)
        except:
            return "Error!"
        finally:
            self.connection.close()
