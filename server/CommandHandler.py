import ast

class Response: 
    def __init__(self, message : str):
        self.message = message
    
    def __dict__(self) -> dict:
        return {
            'message' : self.message
        }

    def __bytes__(self):
        return str(self.__dict__()).encode()

class CommandHandler: 
    def __init__(self):
        pass 

    def process(self, data : bytes) -> Response:
        decoded : dict= ast.literal_eval(data.decode())
        if (not "command" in decoded):
            return Response("Error: Bad JSON received")

        return self.__process_command__(decoded["command"], decoded)

    def __process_command__(self, command : str, decoded : dict) -> Response:
        if (command == "join"):
            return self.__handle_join__(decoded)
    
    def __handle_join__(self, decoded : dict):
        return Response('Connection to the Message Board Server is successful!')