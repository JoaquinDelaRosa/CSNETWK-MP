from ClientModel import * 

class ServerState:
    clients: dict = {}

    def try_register_handle(self, handle : str, addr: tuple) -> bool:
        if self.is_recognized_handle(handle):
            return False 

        self.clients[handle] = ClientModel(addr, handle)
        return True
    
    def is_recognized_handle(self, handle: str) -> bool:
        p_handle = handle.lower()
        if len(p_handle) == 0:
            return False 
        
        return p_handle in [x.lower() for x in self.clients.keys()]
    
    def get_clients(self) -> dict:
        return self.clients

    def get_all_addr(self) -> list:
        return [x.addr for x in self.clients.values()]

    def get_handle_of_addr(self, addr : tuple) -> str:
        for x in self.clients.keys():
            (ip, port) = addr
            (_ip, _port) = self.clients[x].addr
            if ip == _ip and port == _port: 
                return x
        return None
    
    def get_addr_of_handle(self, handle : str) -> tuple:
        return self.clients[handle].addr