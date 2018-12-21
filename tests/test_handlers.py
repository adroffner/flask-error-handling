from flask_error_handling import handlers
import unittest
from unittest import mock
from unittest.mock import Mock, patch, MagicMock
from parameterized import parameterized


class TestHandlers(unittest.TestCase):
    def setUp(self):
        pass

    @parameterized.expand(["400", "401", "402", "403", "404", "405", "406", "407", "408", "409", "410", "411", "412",
                           "413", "414", "415", "416", "417", "500", "501", "502", "503", "504", "505"])
    def test_handlers(self, err_code):
        with mock.patch('flask_error_handling.handlers.handle_error_page', return_value=""):
            func_name = "handlers.handle_error_page_" + err_code
            method = eval(func_name)
            method("abc")
            handlers.handle_error_page.assert_called_with("abc", status=int(err_code))

    def test_handle_error_page(self):
        res, stat = handlers.handle_error_page("abc", 400)
        self.assertEqual(res, '{"message": "abc"}')
        self.assertEqual(stat, 400)

    @patch('flask_error_handling.handlers.log.exception', MagicMock(return_value="Hello"))
    def test_handle_error_page_500(self):
        exc = Mock(side_effect=Exception('Boom!'))
        res, stat = handlers.handle_error_page(exc, 500)
        self.assertEqual(stat, 500)
