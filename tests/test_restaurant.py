import unittest
from app import app
from extras.utilities import Utilities


class TestRestaurant(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_1_create_restaurant(self):
        data = Utilities.read_data_file("restaurant.json", "data/")
        result = self.app.post("/restaurant/create", json=data)
        self.assertEqual(result.status_code, 200)
