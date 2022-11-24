from ClientSocket import *
from CommandResponse import *
from Command import *

class CommandHandler: 
    client_socket = ClientSocket()

    def __init__(self):
        pass 

    def process(self, command : Command):
        payload = command.payload

        if (payload["command"] == "join"):
            return self.client_socket.set_state(ip_address=payload["server_ip_address"], port=payload["port"])

    