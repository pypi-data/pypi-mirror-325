# exceptions.py


# Define exceptions
class IncorrectDirection(Exception):
    def __init__(self):
        super().__init__('The provided direction is incorrect.')
