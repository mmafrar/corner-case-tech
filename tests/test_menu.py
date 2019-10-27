import json
import unittest
from app import app
from extras.utilities import Utilities


class TestMenu(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_1_menu_upload(self):
        data = Utilities.read_data_file("menu.json", "data/")
        result = self.app.post("/menu/upload", json=data)
        self.assertEqual(result.status_code, 200)

    def test_2_get_menu(self):
        data = [{"id": 1, "item": "item1", "description": "description1", "restaurant_id": 1}]
        result = self.app.get("/menu")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.data), data)

    def test_3_menu_vote(self):
        data = {"id": 1}
        result = self.app.post("/menu/vote", json=data)
        self.assertEqual(result.status_code, 200)

    def test_4_menu_results(self):
        data = [{"id": 1, "item": "item1", "description": "description1", "votes": 1, "restaurant_id": 1}]
        result = self.app.get("/menu/results")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.data), data)
