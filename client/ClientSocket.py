import socket
from  CommandResponse import *

class ClientSocket:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip_address = ""
    port = 0

    def __init__(self):
        pass 

    def set_state(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port
        
        self.client_socket.sendto("Hello Server", (self.ip_address, self.port))