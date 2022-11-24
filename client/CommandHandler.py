from ClientSocket import *
from Command import *
from CommandResponse import *
from Logger import *

class CommandHandler: 

    def __init__(self, logger : Logger):
        self.client_socket = ClientSocket()
        self.logger = logger

    def process(self, command : Command):
        if (isinstance(command, Join)):
            join : Join = command
            return self.client_socket.set_state(ip_address= join.server_ip_address, port = join.port)

    