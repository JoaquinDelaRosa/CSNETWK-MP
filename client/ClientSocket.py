import socket
from  CommandResponse import *

class ClientSocket:

    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.ip_address = ""
        self.port = 0

    def set_state(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port
        
        self.client_socket.sendto("Hello World".encode(), (ip_address, port))