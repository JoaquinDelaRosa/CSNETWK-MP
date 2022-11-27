from ChannelModel import *
from ClientModel import * 

class ServerState:
    clients: dict[str, ClientModel] = {}
    channels: dict[str, ChannelModel] = {}

    def try_register_handle(self, handle : str, addr: tuple) -> bool:
        if self.is_recognized_handle(handle):
            return False 

        self.clients[handle] = ClientModel(addr, handle)
        return True
    
    def try_create_channel(self, channel: str, addr: tuple) -> bool:
        handle = self.get_handle_of_addr(addr)
        if not self.is_recognized_handle(handle):
            return False 

        if self.is_recognized_channel(channel):
            return False 
        
        self.channels[channel] = ChannelModel(handle, channel)
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
    
    def get_channels_list_message(self) -> str:
        channels = [c.name for c in self.channels.values()]
        channels.sort()

        return "Channels:\n" + "\n".join(channels)