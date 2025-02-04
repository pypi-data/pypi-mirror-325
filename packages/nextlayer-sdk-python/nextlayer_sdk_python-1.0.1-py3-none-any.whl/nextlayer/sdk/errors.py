class NextlayerSdkError(Exception):
    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        if self.message:
            return self.__class__.__name__ + ": " + str(self.message)
        else:
            return self.__class__.__name__


class AuthenticationError(NextlayerSdkError):
    """Exception raised for authentication errors."""

    pass
