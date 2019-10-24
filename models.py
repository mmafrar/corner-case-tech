import pymysql


class EmployeeModel:
    def __init__(self):
        self.connection = pymysql.connect("localhost", "admin", "admin", "corner_case_tech")

    def create(self, username, email, password):
        cursor = self.connection.cursor()
        query = 'INSERT INTO employee (username, email, password) values (%s, %s, %s)'

        try:
            cursor.execute(query, (username, email, password))
            self.connection.commit()
            return True
        except:
            self.connection.rollback()
            return False
        finally:
            self.connection.close()
