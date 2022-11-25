class ClientModel: 
    def __init__(self, handle: str):
        self.handle = handle
        pass 

class ServerState:
    clients: dict = {}

    def try_register_handle(self, handle : str, addr: tuple) -> bool:
        if self.is_recognized_handle(handle):
            return False 

        self.clients[addr] = ClientModel(handle)
        return True
    
    def is_recognized_handle(self, handle: str) -> bool:
        p_handle = handle.lower()
        if len(p_handle) == 0:
            return False 
        
        return p_handle in [x.handle for x in self.clients.values()]
    
    def get_clients(self) -> dict:
        return self.clients
