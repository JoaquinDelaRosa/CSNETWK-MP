import ast

from ServerState import *
from Response import *
from Validation import *


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

        # Additional commands
        elif command == "channels":
            return self.__handle_channels__(decoded, addr)
        elif command == "createc":
            return self.__handle_createc__(decoded, addr)
        elif command == "invitec":
            return self.__handle_invitec__(decoded, addr)    

        return [Response("Unknown command recieved"), [addr]]
    
    def __handle_join__(self, decoded : dict, sender_addr : tuple):
        return [Response('Connection to the Message Board Server is successful!', [sender_addr])]
    
    def __handle_leave__(self, decoded: dict, sender_addr : tuple):
        return [Response("Connection closed. Thank you!", [sender_addr])]

    def __handle_register__(self, decoded : dict, sender_addr: tuple):
        if not "handle" in decoded: make_bad_form_response("handle", sender_addr)

        handle = decoded["handle"]
        if self.server_state.try_register_handle(handle, sender_addr):
            return [Response("Welcome " + handle, [sender_addr])]

        return [Response("Error: Registration failed. Handle or alias already exists.", [sender_addr])]
    
    def __handle_all__(self, decoded : dict, sender_addr: tuple) : 
        if not "message" in decoded: make_bad_form_response("message", sender_addr)
        
        sender_handle = self.server_state.get_handle_of_addr(sender_addr)
        message = decoded["message"]
        
        if sender_handle == None: 
            return make_unknown_sender(sender_addr)

        return [Response(sender_handle + ": " + message, [addr for addr in self.server_state.get_all_addr()])]
    
    def __handle_msg__(self, decoded : dict, sender_addr : tuple) :
        if not "handle" in decoded: make_bad_form_response("handle", sender_addr)
        if not "message" in decoded: make_bad_form_response("message", sender_addr)
        
        message = decoded["message"]
        reciever_handle = decoded["handle"]

        sender_handle = self.server_state.get_handle_of_addr(sender_addr)
        receiver_addr = self.server_state.get_addr_of_handle(reciever_handle)

        if sender_handle == None: return make_unknown_sender(sender_addr)
        if receiver_addr == None: return make_handle_not_found(sender_addr)
        
        return [
            Response("[To " + reciever_handle + "]: " + message, [sender_addr]),
            Response("[From " + sender_handle + "]: " + message, [receiver_addr])
        ]
    
    def __handle_channels__(self, decoded: dict, sender_addr: tuple):
        message: str = self.server_state.get_channels_list_message()
        return [Response(message, [sender_addr])]
    
    def __handle_createc__(self, decoded: dict, sender_addr: tuple):
        if not "channel" in decoded: make_bad_form_response("channel", sender_addr)
        
        channel : str = decoded["channel"]
        if self.server_state.try_create_channel(channel, sender_addr):
            return [Response("Successfully created channel " + channel, [sender_addr])]

        return [Response("Error: Channel creation failed.", [sender_addr])]
    
    def __handle_invitec__(self, decoded: dict, sender_addr: tuple):
        if not "channel" in decoded: make_bad_form_response("channel", sender_addr)
        if not "handle" in decoded: make_bad_form_response("handle", sender_addr)
        
        channel = decoded["channel"]
        handle = decoded["handle"]

        sender_handle = self.server_state.get_handle_of_addr(sender_addr)
        receiver_addr = self.server_state.get_addr_of_handle(handle)
        
        if sender_handle == None: return make_unknown_sender(sender_addr)
        if receiver_addr == None: return make_handle_not_found(sender_addr)

        channel_model = self.server_state.channels[channel]
        if channel_model == None: return make_channel_not_found(sender_addr)
        
        if channel_model.invite(self.server_state.clients[handle]):
            return [
                Response("> " + channel + ": Invited " + handle, [sender_addr]),
                Response(sender_handle + " is inviting you to " + channel, [receiver_addr])
            ]

        return [Response("Error: Invitation failed.", [sender_addr])]
