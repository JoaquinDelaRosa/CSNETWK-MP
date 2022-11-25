import socket

from CommandHandler import *
from Configs import *
from ServerState import *

class ServerSocket:

    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((IP_ADDRESS, PORT_NUMBER))

        self.server_state = ServerState()
        self.command_handler = CommandHandler(self.server_state)

    def listen(self):
        print("Listening...")
        while True:
            (data, addr) = self.server_socket.recvfrom(1024)
            responses = self.process(data, addr)
            for response in responses:
                for target in response.targets: 
                    self.server_socket.sendto(response.__bytes__(), target)

    def process(self, data, addr):
        print("Received from IP" + str(addr[0]) + " port=" + str(addr[1]))
        print(data)

        return self.command_handler.process(data, addr)
        