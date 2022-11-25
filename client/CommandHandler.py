from ClientSocket import *
from Command import *
from Logger import *


class CommandResponse: 
    message : str
    def __self__(self, message : str):
        self.message = message

class CommandHandler: 

    def __init__(self, logger : Logger, client_socket : ClientSocket):
        self.client_socket = client_socket
        self.logger = logger

    def process(self, command : Command):
        if (isinstance(command, Join)):
            join : Join = command
            self.client_socket.join(ip_address= join.server_ip_address, port = join.port)
        elif (isinstance(command, Leave)):
            leave : Leave = command 
            self.client_socket.leave()
        

    