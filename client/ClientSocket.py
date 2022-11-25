import socket

def encode(dict : dict) -> str:
    return str(dict)

class ClientSocket:

    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.ip_address = ""
        self.port = 0

    def set_state(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port
    
    def send(self, payload):
        self.client_socket.sendto(encode(payload).encode(), (self.ip_address, self.port))

    def listen(self):
        while True:
            try:
                (res, addr) = self.client_socket.recvfrom(1024)
                print(res)
            except: 
                pass