import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login_route(self):
        response = self.app.post('/login', data={'username': 'testuser'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'testuser', response.data)

    def test_yield_route(self):
        response = self.app.get('/yield')
        self.assertEqual(response.status_code, 200)

    def test_predict_route(self):
        response = self.app.post('/predict', data={'data': '50'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Predicted yield', response.data)

if __name__ == '__main__':
    unittest.main()