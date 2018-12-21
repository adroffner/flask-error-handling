""" Register Flask Error Handlers.

Register expected Exception types to HTTP status codes.
This guarantees the HTTP response will have the desired format.

See: Registering Error Handlers
     http://flask.pocoo.org/docs/1.0/errorhandling/#error-handlers

See: Custom Error Pages
     http://flask.pocoo.org/docs/1.0/patterns/errorpages/
"""

import json

import logging
log = logging.getLogger(__name__)


def handle_error_page(exc, status=500):
    """ Handle Error Page.

    This is the general error handler.

    :param Exception exc: raised exception to handle
    """

    # Write an exception log for at least 500-level ones.
    if status > 499:
        try:
            raise exc
        except Exception:
            log.exception('Uncaught Server Error...')

    # Basic Flask expects a str body.
    # JSON Flask_RESTPlus expects a dict body.
    return json.dumps({'message': str(exc)}), status


def handle_error_page_400(exc):
    " Bad Request "
    return handle_error_page(exc, status=400)


def handle_error_page_401(exc):
    " Unauthorized "
    return handle_error_page(exc, status=401)


def handle_error_page_402(exc):
    " Payment Required "
    return handle_error_page(exc, status=402)


def handle_error_page_403(exc):
    " Forbidden "
    return handle_error_page(exc, status=403)


def handle_error_page_404(exc):
    " Not Found "
    return handle_error_page(exc, status=404)


def handle_error_page_405(exc):
    " Method Not Allowed "
    return handle_error_page(exc, status=405)


def handle_error_page_406(exc):
    " Not Acceptable "
    return handle_error_page(exc, status=406)


def handle_error_page_407(exc):
    " Proxy Authentication Required "
    return handle_error_page(exc, status=407)


def handle_error_page_408(exc):
    " Request Timeout "
    return handle_error_page(exc, status=408)


def handle_error_page_409(exc):
    " Conflict "
    return handle_error_page(exc, status=409)


def handle_error_page_410(exc):
    " Gone "
    return handle_error_page(exc, status=410)


def handle_error_page_411(exc):
    " Length Required "
    return handle_error_page(exc, status=411)


def handle_error_page_412(exc):
    " Precondition Failed "
    return handle_error_page(exc, status=412)


def handle_error_page_413(exc):
    " Request Entity Too Large "
    return handle_error_page(exc, status=413)


def handle_error_page_414(exc):
    " Request-URI Too Long "
    return handle_error_page(exc, status=414)


def handle_error_page_415(exc):
    " Unsupported Media Type "
    return handle_error_page(exc, status=415)


def handle_error_page_416(exc):
    " Requested Range Not Satisfiable "
    return handle_error_page(exc, status=416)


def handle_error_page_417(exc):
    " Expectation Failed "
    return handle_error_page(exc, status=417)


def handle_error_page_500(exc):
    " Internal Server Error "
    return handle_error_page(exc, status=500)


def handle_error_page_501(exc):
    " Not Implemented "
    return handle_error_page(exc, status=501)


def handle_error_page_502(exc):
    " Bad Gateway "
    return handle_error_page(exc, status=502)


def handle_error_page_503(exc):
    " Service Unavailable "
    return handle_error_page(exc, status=503)


def handle_error_page_504(exc):
    " Gateway Timeout "
    return handle_error_page(exc, status=504)


def handle_error_page_505(exc):
    " HTTP Version Not Supported "
    return handle_error_page(exc, status=505)
