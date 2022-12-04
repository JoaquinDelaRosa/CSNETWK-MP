class ClientModel: 
    def __init__(self, addr : tuple, handle: str, id : int):
        self.id = id
        self.handle = handle
        self.addr = addr
        self.block_list : list[int] = []
    
    def block(self, client):
        c : ClientModel = client
        self.block_list.append(c.id)
    
    def unblock(self, client):
        c : ClientModel =  client
        if c.id in self.block_list:
            self.block_list.remove(c.id)

    def is_blocked(self, client):
        c : ClientModel = client 
        return c.id in self.block_list 