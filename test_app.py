# test_app.py

import unittest
from app import app

class FlaskAppTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = app.test_client()
        cls.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Hello, World!")

    def test_add_numbers(self):
        response = self.app.post('/add', json={'a': 5, 'b': 3})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 8)

    def test_add_numbers_missing_params(self):
        response = self.app.post('/add', json={'a': 5})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'Missing parameters')

if __name__ == '__main__':
    unittest.main()
