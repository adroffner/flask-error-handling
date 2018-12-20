import unittest
from unittest.mock import Mock, patch, MagicMock
from unittest import mock
from flask_error_handling import bindings


class TestBindings(unittest.TestCase):
    def setUp(self):
        pass

    def test_bind_error_handlers(self):
        register_status_dict = {
            400: ['a', 'b'],
            403: ['c'],
        }
        pl = Mock()
        with mock.patch('flask_error_handling.bindings.register_exceptions', return_value=""):
            bindings.bind_error_handlers(pl, register_status_dict)
            bindings.register_exceptions.assert_called_with(403, ['c'])

    @patch('flask_error_handling.bindings.issubclass', MagicMock(return_value=True))
    def test_register_exceptions(self):
        bindings.HTTP_STATUS_TO_HANDLER = {
            400: "handle_error_page_400",  # Bad Request
            401: "handle_error_page_401",  # Unauthorized
            402: "handle_error_page_402",  # Payment Required
            403: "handle_error_page_403",
        }
        bindings.REGISTERED_EXCEPTIONS = {
            400: ['a'],
            401: [],
            402: [],
            403: ['c']
        }
        bindings.register_exceptions(400, ['a', 'b'])
        self.assertTrue(bindings.REGISTERED_EXCEPTIONS[400], ['a', 'b'])

    @patch('flask_error_handling.bindings.issubclass', MagicMock(return_value=False))
    def test_register_exceptions_error_name(self):
        bindings.HTTP_STATUS_TO_HANDLER = {
            400: "handle_error_page_400",  # Bad Request
            401: "handle_error_page_401",  # Unauthorized
            402: "handle_error_page_402",  # Payment Required
            403: "handle_error_page_403",
        }
        bindings.REGISTERED_EXCEPTIONS = {
            400: ['a', 'x'],
            401: [],
            402: [],
            403: ['c']
        }
        j = Mock()
        try:
            bindings.register_exceptions(400, [j])
        except Exception as e:
            self.assertEqual(str(e), "Cannot register object types [<class 'unittest.mock.Mock'>] as Exception")

    @patch('flask_error_handling.bindings.issubclass', MagicMock(return_value=True))
    def test_register_exceptions_error(self):
        bindings.HTTP_STATUS_TO_HANDLER = {
            400: "handle_error_page_400",  # Bad Request
            401: "handle_error_page_401",  # Unauthorized
            402: "handle_error_page_402",  # Payment Required
            403: "handle_error_page_403",
        }
        bindings.REGISTERED_EXCEPTIONS = {
            400: ['a'],
            401: [],
            402: [],
            403: ['c']
        }
        try:
            bindings.register_exceptions(404, ['a', 'b'])
        except Exception as e:
            self.assertEqual(str(e), "Unsupported HTTP status 404")
