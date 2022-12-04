from ChannelModel import *
from ClientModel import * 

class ServerState:

    current_client_id_ = 0
    clients: dict[str, ClientModel] = {}
    channels: dict[str, ChannelModel] = {}

    def try_register_handle(self, handle : str, addr: tuple) -> bool:
        if self.is_recognized_handle(handle):
            return False 

        self.clients[handle] = ClientModel(addr, handle, self.current_client_id_)
        self.current_client_id_ += 1
        return True
    
    def try_create_channel(self, channel: str, addr: tuple) -> bool:
        owner = self.get_client_by_addr(addr)
        if owner == None:
            return None 

        if not self.is_recognized_handle(owner.handle):
            return False 

        if self.is_recognized_channel(channel):
            return False 
        
        self.channels[channel] = ChannelModel(owner, channel)
        return True
    
    def is_recognized_handle(self, handle: str) -> bool:
        if handle is None:
            return False 

        p_handle = handle.lower()
        if len(p_handle) == 0:
            return False 
        
        return p_handle in [x.lower() for x in self.clients.keys()]
    
    def is_recognized_channel(self, channel: str) -> bool:
        if channel is None:
            return False

        p_channel = channel.lower()
        if len(p_channel) == 0:
            return False 
        
        return p_channel in [c.name.lower() for c in self.channels.values()]
    
    def mutate_channel(self, channel: ChannelModel) -> bool:
        if channel is None:
            return False 
        self.channels[channel.name] = channel

    def mutate_client(self, client: ClientModel) -> bool: 
        if client is None: 
            return False 
        self.clients[client.handle] = client

    def get_clients(self) -> dict:
        return self.clients

    def get_all_addr(self) -> list:
        return [x.addr for x in self.clients.values()]

    def get_client_by_addr(self, addr : tuple) -> ClientModel:
        for x in self.clients.keys():
            (ip, port) = addr
            (_ip, _port) = self.clients[x].addr
            if ip == _ip and port == _port: 
                return self.clients[x]
        
        return None
    
    def get_client_by_handle(self, handle : str) -> ClientModel:
        if handle in self.clients:
            return self.clients[handle]

        return None
    
    def get_channels_list_message(self) -> str:
        channels = [c.name for c in self.channels.values()]
        channels.sort()

        return "Channels:\n" + "\n".join(channels)
    
    def get_channel_by_name(self, name: str) -> ChannelModel:
        if name in self.channels:
            return self.channels[name]
        
        return None

    def get_user_list_message(self) -> str:
        users = [c.handle for c in self.clients.values()]
        users.sort()

        return "Users:\n" + "\n".join(users)
    
    def get_channel_list_user_message(self, name:str) -> str:
        users = [c.handle for c in self.channels[name].get_all()]
        users.sort()

        return "Users in "+name+":\n"+"\n".join(users) 

    def get_user_listblk_message(self, name:str) -> str:
        users_ids = [c for c in self.clients[name].block_list]
        users = []

        #There has to be a list comprehension alternative to this. 
        for i in self.clients.values():
            for j in users_ids:
                if (i.id == j):
                    users.append(i.handle)

        users.sort()

        return "Blocked Users:\n" + "\n".join(users)
        