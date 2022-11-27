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
            user == self.owner

    def get_all(self) -> list[ClientModel]:
        l =  [self.owner]
        l.extend(self.admins)
        l.extend(self.members)

        return l
        

    def is_invited(self, user: ClientModel) -> bool:
        return user in self.invitees
    
    def add_member(self, user: ClientModel) -> bool:
        self.remove(user)
        self.members.append(user)
        
    def remove(self, user : ClientModel) -> bool:
        self.remove_from_invitees(user)
        self.remove_from_members(user)
        self.remove_from_admins(user)

    def remove_from_invitees(self, user: ClientModel):
        if user in self.invitees:
            self.invitees.remove(user)

    def remove_from_members(self, user: ClientModel):
        if user in self.members:
            self.members.remove(user)
    
    def remove_from_admins(self, user: ClientModel):
        if user in self.admins:
            self.admins.remove(user)