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
        elif command == "acceptc":
            return self.__handle_acceptc__(decoded, addr)
        elif command == "declinec":
            return self.__handle_declinec__(decoded, addr)
        elif command == "msgch":
            return self.__handle_msgch__(decoded, addr)

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
        
        sender = self.server_state.get_client_by_addr(sender_addr)
        message = decoded["message"]
        
        if sender == None: 
            return make_unknown_sender(sender_addr)

        return [Response(sender.handle + ": " + message, [addr for addr in self.server_state.get_all_addr()])]
    
    def __handle_msg__(self, decoded : dict, sender_addr : tuple) :
        if not "handle" in decoded: make_bad_form_response("handle", sender_addr)
        if not "message" in decoded: make_bad_form_response("message", sender_addr)
        
        message = decoded["message"]
        reciever_handle = decoded["handle"]

        sender = self.server_state.get_client_by_addr(sender_addr)
        reciever = self.server_state.get_client_by_handle(reciever_handle)

        if sender == None: return make_unknown_sender(sender_addr)
        if reciever == None: return make_handle_not_found(sender_addr)
        
        return [
            Response("[To " + reciever.handle + "]: " + message, [sender.addr]),
            Response("[From " + sender.handle + "]: " + message, [reciever.addr])
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
        receiver_handle = decoded["handle"]

        sender = self.server_state.get_client_by_addr(sender_addr)
        reciever = self.server_state.get_client_by_handle(receiver_handle)

        if sender == None: return make_unknown_sender(sender_addr)
        if reciever == None: return make_handle_not_found(sender_addr)

        channel_model = self.server_state.get_channel_by_name(channel)
        if channel_model == None: return make_channel_not_found(sender_addr)

        if not channel_model.has_pseudo(sender):
            return make_failed_permissions(sender_addr)

        if channel_model.invite(self.server_state.clients[receiver_handle]):
            return [
                Response("> " + channel + ": Invited " + reciever.handle, [sender.addr]),
                Response(sender.handle + " is inviting you to " + channel, [reciever.addr])
            ]

        return [Response("Error: Invitation failed.", [sender_addr])]

    def __handle_acceptc__(self, decoded: dict, sender_addr: tuple):
        if not "channel" in decoded: make_bad_form_response("channel", sender_addr)

        channel = decoded["channel"]

        channel_model = self.server_state.get_channel_by_name(channel)
        if channel_model == None: return make_channel_not_found(sender_addr)

        sender = self.server_state.get_client_by_addr(sender_addr)
        receiver = self.server_state.channels[channel].owner

        if sender == None: return make_unknown_sender(sender_addr)
        if receiver == None: return make_handle_not_found(sender_addr)
        
        print(receiver)
        if sender == receiver: 
            return [Response("Error: Server owner cannot accept or reject because they are always in the channel"), [sender.addr]]

        if channel_model.is_invited(sender):
            channel_model.add_member(sender)
            return [
                Response("> Invite to " + channel + " acknowledged. Welcome! ", [sender.addr]),
                Response("> "+ sender.handle + "accepted your invite.", [receiver.addr])
            ]

        return [Response("Error: Acceptance failed.", [sender_addr])]

    def __handle_declinec__(self, decoded: dict, sender_addr: tuple):
        if not "channel" in decoded: make_bad_form_response("channel", sender_addr)

        channel = decoded["channel"]

        channel_model = self.server_state.get_channel_by_name(channel)
        if channel_model == None: return make_channel_not_found(sender_addr)

        sender = self.server_state.get_client_by_addr(sender_addr)
        receiver = self.server_state.channels[channel].owner

        if sender == None: return make_unknown_sender(sender_addr)
        if receiver == None: return make_handle_not_found(sender_addr)
        
        if sender == receiver: 
            return [Response("Error: Server owner cannot accept or reject because they are always in a channel"), [sender.addr]]

        if channel_model.is_invited(sender):
            channel_model.remove_from_invitees(sender)
            return [
                Response("> Invite to " + channel + " declined.", [sender_addr]),
                Response("> "+ sender.handle + "declined your invite.", [receiver.addr])
            ]

        return [Response("Error: Acceptance failed.", [sender_addr])]
    
    def __handle_msgch__(self, decoded : dict, sender_addr : tuple) :
        if not "channel" in decoded: make_bad_form_response("channel", sender_addr)
        if not "message" in decoded: make_bad_form_response("message", sender_addr)
        
        channel = decoded["channel"]
        message = decoded["message"]

        sender = self.server_state.get_client_by_addr(sender_addr)
        reciever_channel = self.server_state.get_channel_by_name(channel)

        if sender == None: return make_unknown_sender(sender_addr)
        if reciever_channel == None: return make_channel_not_found(sender_addr)
        
        return [
            Response("[To <" + reciever_channel.name + ">]: " + message, [sender.addr]),
            Response("[From " + sender.handle + "]: " + message, reciever_channel.get_all())
        ]