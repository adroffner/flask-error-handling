""" Flask Exception Handling Examples.
"""


class ForbiddenRouteError(Exception):
    """ Forbidden Route Error.

    This route is fobidden to the current user.
    """

    def __init__(self, *args, **kwargs):
        """ Init ForbiddenRouteError.
        """

        super().__init__('You are forbidden!')
