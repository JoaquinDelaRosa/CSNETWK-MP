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

        self.is_connected = False

    def join(self, ip_address, port):
        self.send(ip_address, port, {'command' : 'join'})
        self.__confirm_connection__()
    
    def send(self, ip_address, port, payload):
        self.client_socket.sendto(encode(payload).encode(), (ip_address, port))

    def listen(self):
        while True:
            try:
                (res, addr) = self.client_socket.recvfrom(1024)
                self.logger.log(get_response_message(res))

            except TimeoutError:
                pass
    
    def __confirm_connection__(self):
        try:
            (res, addr) = self.client_socket.recvfrom(1024)
            self.logger.log(get_response_message(res))
            self.is_connected = True

        except TimeoutError:
            self.logger.log("Error: Connection to the Message Board Server has failed! Please check IP Address and Port Number")