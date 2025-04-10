import unittest
from app import create_app

class TestCalculatorAPI(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()
        self.app.testing = True

    def test_add(self):
        response = self.app.get('/add?a=2&b=3')
        self.assertEqual(response.get_json()['result'], 5)

if __name__ == '__main__':
    unittest.main()
