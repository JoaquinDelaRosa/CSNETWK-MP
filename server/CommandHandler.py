import ast

from ServerState import *

class Response: 
    def __init__(self, message : str, targets : list[tuple]):
        self.message = message
        self.targets =targets
    
    def __dict__(self) -> dict:
        return {
            'message' : self.message
        }

    def __bytes__(self):
        return str(self.__dict__()).encode()
    
    def get_targets(self):
        return self.targets

class CommandHandler: 
    def __init__(self, server_state : ServerState):
        self.server_state = server_state

    def process(self, data : bytes, addr : tuple) -> Response:
        decoded : dict= ast.literal_eval(data.decode())
        if not "command" in decoded:
            return Response("Error: Bad JSON received")

        return self.__process_command__(decoded["command"], decoded, addr)

    def __process_command__(self, command : str, decoded : dict, addr : tuple) -> list[Response]:
        if command == "join":
            return self.__handle_join__(decoded, addr)
        elif command == "leave":
            return self.__handle_leave__(decoded, addr)
        elif command == "register":
            return self.__handle_register__(decoded, addr)
        elif command == "all":
            return self.__handle_all__(decoded, addr)
        elif command == "msg":
            return self.__handle_msg__(decoded, addr)

        return Response("Unknown command recieved")
    
    def __handle_join__(self, decoded : dict, addr : tuple):
        return [Response('Connection to the Message Board Server is successful!', [addr])]
    
    def __handle_leave__(self, decoded: dict, addr : tuple):
        return [Response("Connection closed. Thank you!", [addr])]

    def __handle_register__(self, decoded : dict, addr: tuple):
        if not "handle" in decoded:
            return [Response("Error: Received object is in bad form. Expecting 'handle' as a keyword", [addr])]

        handle = decoded["handle"]
        if self.server_state.try_register_handle(handle, addr):
            return [Response("Welcome " + handle, [addr])]

        return [Response("Error: Registration failed. Handle or alias already exists.", [addr])]
    
    def __handle_all__(self, decoded : dict, addr: tuple) : 
        if not "message" in decoded:
            return [Response("Error: Received object is in bad form. Expecting 'message' as a keyword", [addr])]
        
        handle = self.server_state.get_handle_of_addr(addr)
        message = decoded["message"]
        return [Response(handle + ": " + message, [addr for addr in self.server_state.get_all_addr()])]
    
    def __handle_msg__(self, decoded : dict, sender_addr : tuple) :
        if not "handle" in decoded:
            return [Response("Error: Received object is in bad form. Expecting 'handle' as a keyword", [sender_addr])]
        if not "message" in decoded:
            return [Response("Error: Received object is in bad form. Expecting 'message' as a keyword", [sender_addr])]
        
        message = decoded["message"]
        
        reciever_handle = decoded["handle"]
        sender_handle = self.server_state.get_handle_of_addr(sender_addr)
        receiver_addr = self.server_state.get_addr_of_handle(reciever_handle)

        if receiver_addr == None: 
            return [Response("Error: Handle or alias not found.", [sender_addr])]
        
        return [
            Response("[To " + reciever_handle + "]: " + message, [sender_addr]),
            Response("[From " + sender_handle + "]: " + message, [receiver_addr])
        ]
        
        
        