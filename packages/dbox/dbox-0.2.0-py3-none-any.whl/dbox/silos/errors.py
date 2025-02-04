class AppError(Exception):
    def __init__(self, *, message=None):
        self.message = message

    def get_message(self):
        return self.message or "unknown error"


def fail(message):
    raise AppError(message=message)
