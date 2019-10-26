import json, unittest
from app import app


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_employee(self):
        data = {"username": "user1", "email": "user1@email.com", "password": "password1"}
        result = self.app.post("/employee/create", json=data)
        self.assertEqual(result.status_code, 200)


class TestRestaurant(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_restaurant(self):
        data = {"name": "restaurant1", "telephone": "telephone1"}
        result = self.app.post("/restaurant/create", json=data)
        self.assertEqual(result.status_code, 200)


class TestMenu(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_menu_upload(self):
        data = {"item": "item1", "description": "description1", "restaurant_id": "1"}
        result = self.app.post("/menu/upload", json=data)
        self.assertEqual(result.status_code, 200)

    def test_get_menu(self):
        data = [{"id": 1, "item": "item1", "description": "description1", "restaurant_id": 1}]
        result = self.app.get("/menu")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.data), data)

    def test_menu_vote(self):
        data = {"id": 1}
        result = self.app.post("/menu/vote", json=data)
        self.assertEqual(result.status_code, 200)

    def test_menu_results(self):
        data = [{"id": 1, "item": "item1", "description": "description1", "votes": 1, "restaurant_id": 1}]
        result = self.app.get("/menu/results")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.data), data)
