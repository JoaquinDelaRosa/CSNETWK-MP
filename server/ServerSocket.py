import socket

from CommandHandler import *
from Configs import *
from ServerState import *

class ServerSocket:

    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((IP_ADDRESS, PORT_NUMBER))

        self.command_handler = CommandHandler()

    def listen(self):
        print("Listening...")
        while True:

            try: 
                (data, addr) = self.server_socket.recvfrom(1024)
                responses = self.process(data, addr)
                for response in responses:
                    for target in response.targets: 

                        if ALLOW_BLOCKING_PROTOCOL:
                            state = self.__get_state__()
                            sender = state.get_client_by_addr(addr)
                            receiver = state.get_client_by_addr(target)
                            
                            if not sender is None and not receiver is None: 
                                if receiver.is_blocked(sender):
                                    continue

                        self.server_socket.sendto(response.__bytes__(), target)
            except:
                # Graceful exit
                continue 

    def process(self, data, addr) -> list[Response]:
        print("Received from IP " + str(addr[0]) + " port=" + str(addr[1]))
        print(data)

        result = self.command_handler.process(data, addr)
        return result
    
    def __get_state__(self):
        return self.command_handler.server_state
        