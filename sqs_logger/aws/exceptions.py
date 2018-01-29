class QueueError(Exception):
    message = 'Internal server error'

    def __init__(self, message=None):
        if message:
            self.message = message

    def __str__(self):
        return '{name}'.format(name=self.__class__.__name__)
