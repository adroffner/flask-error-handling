# Flask Error Handling

This is an **error handling** library for **Flask** Web applications.

* See: [Flask Error Pages](http://flask.pocoo.org/docs/1.0/patterns/errorpages/)

- An error handler function returns a Flask response when some type of error is raised.
- An error handler must be registered with Flask.
  - The @app.errorhandler() decorator
  - The app.register_error_handler() method
- A handler can be registered for a status code, like 404, or an Exception subclass.

## @app.errorhandler() decorator

```sh
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404
```

## app.register_error_handler() method

```sh
def page_not_found(e):
  return render_template('404.html'), 404

def create_app(config_filename):
    app = Flask(__name__)
    app.register_error_handler(404, page_not_found)
    return app
```

#### Flask_RESTPlus

The flask_restful.Api constructor also allows an errors dict to map Exception type names, message dict objects, and HTTP status.

* See [Define Custom Error Messages](https://flask-restful.readthedocs.io/en/0.3.5/extending.html#define-custom-error-messages)

```sh
errors = {
    'ResourceDoesNotExist': {
        'message': "A resource with that ID no longer exists.",
        'status': 410,
        'extra': "Any extra information you want.",
    },
}

app = Flask(__name__)
api = flask_restful.Api(app, errors=errors)
```

### Flask Error Handling Usage

This Flask Error Handling library extends the above rules. The **bind_error_handlers** call connects the Flask **app** object to the **REGISTERED_EXC** dictionary. Each HTTP status key has a list of Exception subclass types to register.

1. Add  **flask_error_handling** package to the requirement.txt file.
2. Import the bind_error_handlers function from the package and call it.

#### Example

Create a **REGISTERED_EXC** dictionary and decide which exception to trap as HTTP status.
AgeFormatError, UnderAgeError and ForbiddenRouteError are exceptions defined in the project.

```sh
from flask_error_handling.bindings import bind_error_handlers

REGISTERED_EXC = {
    400: [AgeFormatError, UnderAgeError],
    403: [ForbiddenRouteError],
}


bind_error_handlers(app, register_status_dict=REGISTERED_EXC)
```
