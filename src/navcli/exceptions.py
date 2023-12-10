class RouteNotFound(BaseException):
    """Exception raised for errors in the input.

    Attributes:
    ----------
        route -- input route which caused the error
        message -- explanation of the error
    """

    def __init__(self, route):
        self.route = route
        self.message = f"Route '{route}' not found."

    def __str__(self):
        return self.message


class UnexpectedActionException(BaseException):
    """Exception raised for errors in the input.

    Attributes:
    ----------
        action -- input action which caused the error
        message -- explanation of the error
    """

    def __init__(self, action):
        self.action = action
        self.message = f"Unexpected action '{action}'."

    def __str__(self):
        return self.message
