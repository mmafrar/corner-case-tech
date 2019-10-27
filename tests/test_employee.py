import unittest
from app import app
from extras.utilities import Utilities


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_1_create_employee(self):
        data = Utilities.read_data_file("employee.json", "data/")
        result = self.app.post("/employee/create", json=data)
        self.assertEqual(result.status_code, 200)
