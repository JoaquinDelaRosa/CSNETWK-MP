import socket
import threading
import json 

from Logger import *
from Utils import * 

def encode(dict : dict) -> str:
    return json.dumps(dict)

class ClientSocket:

    def __init__(self, logger : Logger):
        self.logger = logger 

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client_socket.settimeout(1)

        self.connected_ip_address = None 
        self.connected_port = None
        self.output_thread = None

        self.joining_state = False 
        self.leaving_state = False

    def join(self, ip_address : str, port : int):
        self.joining_state = True
        self.connected_ip_address = ip_address
        self.connected_port = port

        self.send({'command' : 'join'})
        if self.__confirm_connection__():
            self.listen()
        
        self.joining_state = False

    def leave(self):
        self.leaving_state = True 

        if self.connected_ip_address is None or self.connected_port is None:
            self.logger.log("Error: Disconnection failed. Please connect to the server first.")
        else: 
            self.send({'command': 'leave'} )
            self.__confirm_disconnection__()
        
        self.leaving_state = False
    
    def send(self, payload):
        if payload is None or self.connected_ip_address is None or self.connected_port is None:
            self.logger.log("Error: Request failed. Please connect to the server first.")
            return 
        
        try: 
            self.client_socket.sendto(encode(payload).encode(), (self.connected_ip_address, self.connected_port))
        except: 
            # Graceful exit.
            self.logger.log("Error: Request failed. Please check the connection to the server.")
            return 

    def listen(self):
        if self.output_thread is None:
            self.client_socket.settimeout(1)
            self.output_thread = threading.Thread(target=self.__listen__)
            self.output_thread.start()

    def __listen__(self):
        while not self.connected_ip_address is None and not self.connected_port is None : 
            try:
                (res, addr) = self.client_socket.recvfrom(1024)

                if self.joining_state:
                    continue 
                if self.leaving_state:
                    self.__update_to_disconnect_state__()
                    continue 

                self.logger.log(get_response_message(res))

            except socket.timeout:
                continue

            except:
                print("Server took too long. It might be down.") # Gracefully ignore when server is down.
    
    def __confirm_connection__(self):
        try:
            (res, addr) = self.client_socket.recvfrom(1024)
            self.logger.log(get_response_message(res))
            self.__update_to_connect_state__(addr)
            return True

        except socket.timeout as err:
            self.logger.log("Error: Connection to the Message Board Server has failed! Please check IP Address and Port Number")
            self.__update_to_disconnect_state__()

            return False

        except:
            # Graceful exit. 
            self.logger.log("Error: Connection to the Message Board Server has failed! Please check IP Address and Port Number.")
            self.__update_to_disconnect_state__()

            return False
        
    
    def __confirm_disconnection__(self):
        try:
            (res, addr) = self.client_socket.recvfrom(1024)
            self.logger.log(get_response_message(res))
            self.__update_to_disconnect_state__()
            return 

        except socket.timeout as err:
            if self.connected_ip_address is None:
                return
                
            self.logger.log("Request Timed Out")
            return 
        
        except:
            return 

    def __update_to_connect_state__(self, addr):
        self.connected_ip_address = str(addr[0])
        self.connected_port = int(str(addr[1]))

    def __update_to_disconnect_state__(self):
        self.client_socket.settimeout(1)
        self.connected_ip_address = None 
        self.connected_port = None
        self.output_thread = None