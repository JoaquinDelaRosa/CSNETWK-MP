from ClientModel import * 

class ChannelModel: 
    def __init__(self, owner: ClientModel , name: str):
        self.owner = owner 
        self.name = name 

        self.admins : list[ClientModel] = []
        self.members : list[ClientModel] = []
        self.invitees: list[ClientModel] = []

    def invite(self, user: ClientModel) -> bool: 
        if self.has_pseudo(user):
            return False 

        self.invitees.append(user)
        return True 

    def has_pseudo(self, user: ClientModel) -> bool:
        return user in self.admins or \
            user in self.members or \
            user in self.invitees or \
            user.handle == self.owner
