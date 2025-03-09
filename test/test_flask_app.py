import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to Flask Server', response.data)

    def test_greet_api(self):
        response = self.app.get('/api/greet?name=Quân')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello, Quân!', response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
