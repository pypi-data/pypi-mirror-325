class AppError(Exception):
    def __init__(self, *, message=None, code=500):
        self.message = message
        self.code = code

    def get_message(self):
        return self.message or "unknown error"


def fail(message, *, code=500):
    raise AppError(message=message, code=code)
