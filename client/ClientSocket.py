import socket
import threading

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
        self.output_thread = None

    def join(self, ip_address : str, port : int):
        if not self.connected_ip_address is None or not self.connected_port is None:
            self.logger.log("Already Connected to a server! Disconnect first")
            return

        self.connected_ip_address = ip_address
        self.connected_port = port

        self.send({'command' : 'join'})
        self.__confirm_connection__()

    def leave(self):
        if self.connected_ip_address is None or self.connected_port is None:
            self.logger.log("Error: Disconnection failed. Please connect to the server first.")
        else: 
            self.send({'command': 'leave'} )
            self.__confirm_disconnection__()
    
    def send(self, payload):
        if payload is None or self.connected_ip_address is None or self.connected_port is None:
            self.logger.log("Error: Request failed. Please connect to the server first.")
            return 

        self.client_socket.sendto(encode(payload).encode(), (self.connected_ip_address, self.connected_port))

    def listen(self):
        if self.output_thread is None:
            self.output_thread = threading.Thread(target=self.__listen__)
            self.output_thread.start()

    def __listen__(self):
        while not self.connected_ip_address is None and not self.connected_port is None : 
            try:
                (res, addr) = self.client_socket.recvfrom(1024)
                self.logger.log(get_response_message(res))
            except socket.timeout:
                pass
    
    def __confirm_connection__(self):
        try:
            (res, addr) = self.client_socket.recvfrom(1024)
            self.logger.log(get_response_message(res))
            self.__update_to_connect_state__(addr)
            self.listen()

        except socket.timeout:
            self.logger.log("Error: Connection to the Message Board Server has failed! Please check IP Address and Port Number")
            self.__update_to_disconnect_state__()
    
    def __confirm_disconnection__(self):
        try:
            (res, addr) = self.client_socket.recvfrom(1024)
            self.logger.log(get_response_message(res))
            self.__update_to_disconnect_state__()

        except socket.timeout:
            self.logger.log("Request Timed Out")

    def __update_to_connect_state__(self, addr):
        self.connected_ip_address = str(addr[0])
        self.connected_port = int(str(addr[1]))

    def __update_to_disconnect_state__(self):
        self.connected_ip_address = None 
        self.connected_port = None
        self.output_thread = None