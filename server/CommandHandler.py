import ast

from ServerState import *

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
    def __init__(self, server_state : ServerState):
        self.server_state = server_state

    def process(self, data : bytes) -> Response:
        decoded : dict= ast.literal_eval(data.decode())
        if not "command" in decoded:
            return Response("Error: Bad JSON received")

        return self.__process_command__(decoded["command"], decoded)

    def __process_command__(self, command : str, decoded : dict) -> Response:
        if command == "join":
            return self.__handle_join__(decoded)
        elif command == "leave":
            return self.__handle_leave__(decoded)
        elif command == "register":
            return self.__handle_register__(decoded)
        elif command == "all":
            return self.__handle_all__(decoded)

        return Response("Unknown command recieved")
    
    def __handle_join__(self, decoded : dict):
        return Response('Connection to the Message Board Server is successful!')
    
    def __handle_leave__(self, decoded: dict):
        return Response("Connection closed. Thank you!")

    def __handle_register__(self, decoded : dict):
        if not "handle" in decoded:
            return Response("Error: Received object is in bad form. Expecting 'handle' as a keyword")

        handle = decoded["handle"]
        if self.server_state.try_register_handle(handle):
            return Response("Welcome " + handle)

        return Response("Error: Registration failed. Handle or alias already exists.")
    
    def __handle_all__(self, decoded) : 
        pass