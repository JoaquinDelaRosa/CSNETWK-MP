class ClientModel: 
    def __init__(self, addr : tuple, handle: str):
        self.handle = handle
        self.addr = addr
        pass 

class ServerState:
    clients: dict = {}

    def try_register_handle(self, handle : str, addr: tuple) -> bool:
        if self.is_recognized_handle(handle):
            return False 

        self.clients[addr] = ClientModel(addr, handle)
        return True
    
    def is_recognized_handle(self, handle: str) -> bool:
        p_handle = handle.lower()
        if len(p_handle) == 0:
            return False 
        
        return p_handle in [x.handle for x in self.clients.values()]
    
    def get_clients(self) -> dict:
        return self.clients

    def get_handle_of_addr(self, addr : tuple) -> str:
        return self.clients[addr].handle
    
    def get_addr_of_handle(self, handle : str) -> tuple:
        for addr in self.clients.keys():
            client = self.clients[addr]
            if client.handle == handle: 
                return addr
        return None