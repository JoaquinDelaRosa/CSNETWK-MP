import ast
import socket

from Logger import *
from Utils import * 

def encode(dict : dict) -> str:
    return str(dict)

class ClientSocket:

    def __init__(self, logger : Logger):
        self.logger = logger 

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client_socket.settimeout(1)

        self.connected_ip_address = None 
        self.connected_port = None

    def join(self, ip_address, port):
        self.send(ip_address, port, {'command' : 'join'})
        self.__confirm_connection__()

    def leave(self):
        if self.connected_ip_address is None or self.connected_port is None:
            self.logger.log("Error: Disconnection failed. Please connect to the server first.")
        else: 
            self.send(self.connected_ip_address, self.connected_port, {'command': 'leave'} )
            self.__confirm_disconnection__()
    
    def send(self, ip_address, port, payload):
        self.client_socket.sendto(encode(payload).encode(), (ip_address, port))

    def listen(self):
        pass
    
    def __confirm_connection__(self):
        try:
            (res, addr) = self.client_socket.recvfrom(1024)
            self.logger.log(get_response_message(res))

            self.connected_ip_address = str(addr[0])
            self.connected_port = int(str(addr[1]))

        except TimeoutError:
            self.logger.log("Error: Connection to the Message Board Server has failed! Please check IP Address and Port Number")
    
    def __confirm_disconnection__(self):
        try:
            (res, addr) = self.client_socket.recvfrom(1024)
            self.logger.log(get_response_message(res))

            self.connected_ip_address = None 
            self.connected_port = None

        except TimeoutError:
            self.logger.log("Request Timed Out")