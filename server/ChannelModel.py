from ClientModel import * 

class ChannelModel: 
    def __init__(self, owner: ClientModel , name: str):
        self.owner = owner 
        self.name = name 

        self.admins : list[ClientModel]
        self.members : list[ClientModel] 