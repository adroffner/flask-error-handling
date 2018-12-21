import unittest
from unittest import skipIf

try:
    from tests.flask_app import server
    HAS_FLASK = True
except ImportError:
    HAS_FLASK = False


@skipIf(not HAS_FLASK, 'Flask library not installed')
class TestFlaskApp(unittest.TestCase):
    """Flask Error Handling

    Prove that the custom errors are registered
    """

    def setUp(self):
        self.maxDiff = None
        server.app.testing = True
        self.client = server.app.test_client()

    def test_custom_error_raised(self):
        res = self.client.get('/restricted/nobody')
        self.assertEqual(res.status_code, 403)
        self.assertEqual(res.data.decode('utf-8'), '{"message": "You are forbidden!"}')

    def test_custom_success(self):
        res = self.client.get('/restricted/john')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data.decode('utf-8'), 'Welcome.')
