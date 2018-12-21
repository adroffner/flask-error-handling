from flask import Flask
from flask_error_handling.bindings import bind_error_handlers

from tests.flask_app.exceptions import (
    ForbiddenRouteError
)

app = Flask(__name__)

# Trapping Flask Exceptions that are not HTTP 500.
REGISTERED_EXC = {
    403: [ForbiddenRouteError]
}
bind_error_handlers(app, register_status_dict=REGISTERED_EXC)


@app.route('/restricted/<string:username>', methods=['GET'])
def goodbye_intruder(username):
    if username == 'nobody':
        raise ForbiddenRouteError()

    return 'Welcome.', 200


if __name__ == '__main__':
    app.run()
