from flask_error_handling.exceptions import InvalidServerErrorsList, UnsupportedHTTPStatus
import unittest
from unittest.mock import Mock


class TestExceptions(unittest.TestCase):
    def setUp(self):
        pass

    def test_raise_unsuppported_status(self):
        obj_1 = UnsupportedHTTPStatus(999)
        self.assertEqual(str(obj_1), "Unsupported HTTP status 999")

    def test_raise_invalid_error(self):
        k = Mock()
        obj_1 = InvalidServerErrorsList([k])
        self.assertEqual(str(obj_1), "Cannot register object types [<class 'unittest.mock.Mock'>] as Exception")
