import socket

from Configs import *

class ServerSocket:

    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((IP_ADDRESS, PORT_NUMBER))

    def listen(self):
        print("Listening...")
        while True:
            (data, addr) = self.server_socket.recvfrom(1024)
            print(data)