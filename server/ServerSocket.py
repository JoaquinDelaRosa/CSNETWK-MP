import socket

from CommandHandler import *
from Configs import *

class ServerSocket:

    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((IP_ADDRESS, PORT_NUMBER))

        self.command_handler = CommandHandler()

    def listen(self):
        print("Listening...")
        while True:
            (data, addr) = self.server_socket.recvfrom(1024)
            response = self.process(data, addr)

            self.server_socket.sendto(response.__bytes__(), addr)

    def process(self, data, addr):
        print("Received from IP" + str(addr[0]) + " port=" + str(addr[1]))
        print(data)

        return self.command_handler.process(data)
        