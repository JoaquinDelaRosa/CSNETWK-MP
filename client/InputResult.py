class InputResult: 
    message: str
    payload = dict()

    def __init__(self, message : str, payload : dict = {}):
        self.message = message
        self.payload = payload

    def __str__(self):
        return self.message


COMMAND_NOT_FOUND_ERROR = InputResult(message="Error: Command Not Found.")
COMMAND_BAD_SYNTAX_ERROR = InputResult(message="Command parameters do not match or is not allowed.")
