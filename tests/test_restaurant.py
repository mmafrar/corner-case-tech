import unittest
from app import app


class TestRestaurant(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_restaurant(self):
        data = {"name": "restaurant1", "telephone": "telephone1"}
        result = self.app.post("/restaurant/create", json=data)
        self.assertEqual(result.status_code, 200)
