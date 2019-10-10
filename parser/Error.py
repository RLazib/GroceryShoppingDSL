class Error(Exception):
    pass


class ParseError(Error):

    def __init__(self, message):
        self.message = message
