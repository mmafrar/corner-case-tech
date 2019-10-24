import json, pymysql
from datetime import date


class EmployeeModel:
    def __init__(self):
        self.connection = pymysql.connect("localhost", "admin", "admin", "corner_case_tech")

    def create(self, username, email, password):
        cursor = self.connection.cursor()
        query = 'INSERT INTO employee (username, email, password) values (%s, %s, %s)'

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
        self.connection = pymysql.connect("localhost", "admin", "admin", "corner_case_tech")

    def create(self, name, telephone):
        cursor = self.connection.cursor()
        query = 'INSERT INTO restaurant (name, telephone) values (%s, %s)'

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
        self.connection = pymysql.connect("localhost", "admin", "admin", "corner_case_tech")

    def upload(self, item, description, restaurant_id):
        cursor = self.connection.cursor()
        _date = date.today()
        query = 'INSERT INTO menu (item, description, restaurant_id, _date) values (%s, %s, %s, %s)'

        try:
            cursor.execute(query, (item, description, restaurant_id, _date))
            self.connection.commit()
            return "Success!"
        except:
            self.connection.rollback()
            return "Error!"
        finally:
            self.connection.close()

    def get(self):
        cursor = self.connection.cursor()
        _date = date.today()
        query = 'SELECT id, item, description, restaurant_id FROM menu WHERE _date=%s'

        try:
            cursor.execute(query, (_date,))
            row_headers = [x[0] for x in cursor.description]
            result = cursor.fetchall()
            json_data = []
            for row in result:
                json_data.append(dict(zip(row_headers, row)))
            return json.dumps(json_data)
        except:
            return "Error!"
        finally:
            self.connection.close()
