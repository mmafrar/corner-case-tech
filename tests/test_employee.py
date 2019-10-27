import unittest
from app import app


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_employee(self):
        data = {"username": "user1", "email": "user1@email.com", "password": "password1"}
        result = self.app.post("/employee/create", json=data)
        self.assertEqual(result.status_code, 200)
