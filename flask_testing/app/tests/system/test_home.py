from unittest import TestCase
from app import app
import json

class TestHome(TestCase):
    def test_home(self):
        with app.test_client() as c:
            res = c.get('/')
            self.assertEqual(res.status_code, 200)
            self.assertEqual(json.loads(res.get_data()), {'message': 'Hello, World!'})
            

