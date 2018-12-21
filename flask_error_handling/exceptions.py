""" Register Flask Error Handlers.

Register expected Exception types to HTTP status codes.
This guarantees the HTTP response will have the desired format.

See: Registering Error Handlers
     http://flask.pocoo.org/docs/1.0/errorhandling/#error-handlers

See: Custom Error Pages
     http://flask.pocoo.org/docs/1.0/patterns/errorpages/
"""


class InvalidServerErrorsList(ValueError):
    """ Invalid Server Errors List.

    A server errors (exceptions) list must contain only Exception subclasses.
    """

    def __init__(self, invalid_objects):
        invalid_object_types = [type(v) for v in invalid_objects]
        super().__init__('Cannot register object types {} as Exception'.format(
            invalid_object_types))


class UnsupportedHTTPStatus(ValueError):
    """ Unsupported HTTP Status Code.

    Only the explicitly listed HTTP codes are supported.
    Requests to add other HTTP codes are welcome.

    Certain status code should never be supported.
        402 "Payment Required"
        418 "I'm a teapot"
    """

    def __init__(self, status_code):
        super().__init__('Unsupported HTTP status {}'.format(status_code))
