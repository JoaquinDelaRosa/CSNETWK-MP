import ast
import socket

from Logger import *

def encode(dict : dict) -> str:
    return str(dict)

class ClientSocket:

    def __init__(self, logger : Logger):
        self.logger = logger 

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client_socket.settimeout(1)
        self.ip_address = ""
        self.port = 0

    def join(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port

        self.send({'command' : 'join'})
        self.__confirm_connection__()
    
    def send(self, payload):
        self.client_socket.sendto(encode(payload).encode(), (self.ip_address, self.port))

    def listen(self):
        while True:
            try:
                (res, addr) = self.client_socket.recvfrom(1024)
                self.logger.log(ast.literal_eval(res.decode()))

            except TimeoutError:
                pass
    
    def __confirm_connection__(self):
        try:
            (res, addr) = self.client_socket.recvfrom(1024)
            self.logger.log(ast.literal_eval(res.decode()))

        except TimeoutError:
            self.logger.log("Error: Connection to the Message Board Server has failed! Please check IP Address and Port Number")