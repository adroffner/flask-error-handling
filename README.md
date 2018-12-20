# Flask Error Handling
=============================

This is an **error handling** library for **Flask** Web applications.
(http://flask.pocoo.org/docs/1.0/patterns/errorpages/)
- An error handler is a function that returns a response when a type of error is raised.
- An error handler is registered with the errorhandler() decorator or the register_error_handler() method.
- A handler can be registered for a status code, like 404, or for an exception class.

```sh
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404
```
```sh
def page_not_found(e):
  return render_template('404.html'), 404

def create_app(config_filename):
    app = Flask(__name__)
    app.register_error_handler(404, page_not_found)
    return app
```

#### Flask_RESTPlus

The flask_restful.Api constructor also allows an errors dict that maps Exception type names (str) to the message dict objects and HTTP status
(https://flask-restful.readthedocs.io/en/0.3.5/extending.html#define-custom-error-messages)

```sh
errors = {
    'ResourceDoesNotExist': {
        'message': "A resource with that ID no longer exists.",
        'status': 410,
        'extra': "Any extra information you want.",
    },
}
```

```sh
app = Flask(__name__)
api = flask_restful.Api(app, errors=errors)
```
### USAGE
- Add  **flask_error_handling** package to the requirement.txt file.
- Import the bind_error_handlers function from the package and call it.
```sh
from flask_error_handling.bindings import bind_error_handlers

bind_error_handlers(app, register_status_dict=REGISTERED_EXC)
```
where

```sh
REGISTERED_EXC = {
    400: [AgeFormatError, UnderAgeError],
    403: [ForbiddenRouteError],
}
```
AgeFormatError, UnderAgeError and ForbiddenRouteError are exceptions defined in the project repository.
