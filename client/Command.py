class Command: 
    command: str

    def __init__(self, command: str):
        self.command = command
    
    def get_payload(self):
        return {
            "command": self.command
        }

class Join(Command):

    def __init__(self, server_ip_address, port):
        self.server_ip_address = server_ip_address
        self.port =port
        Command.__init__(self, "join")
    
    def get_payload(self):
        return {
            "command": "join"
        }

class Leave(Command):

    def __init__(self):
        Command.__init__(self, "leave")
    
    def get_payload(self):
        return {
            "command": "leave"
        }

class Register(Command):

    def __init__(self, handle : str):
        self.handle = handle
        Command.__init__(self, "register")
    
    def get_payload(self):
        return {
            "command": "register",
            "handle": self.handle
        }

class All(Command):

    def __init__(self, message : str):
        self.message = message 
        Command.__init__(self, "all")
    
    def get_payload(self):
        return {
            "command": "all",
            "message": self.message
        }

class Msg(Command):

    def __init__(self, handle : str, message : str):
        self.handle = handle
        self.message = message 
        Command.__init__(self, "msg")
    
    def get_payload(self):
        return {
            "command": "msg",
            "handle": self.handle,
            "message": self.message
        }

class Channels(Command):
    def __init__(self):
        Command.__init__(self, "channels")

    def get_payload(self):
        return {
            "command": "channels"
        }

class Createc(Command):
    def __init__(self, channel : str):
        self.channel = channel
        Command.__init__(self, "createc")

    def get_payload(self):
        return {
            "command": "createc",
            "channel": self.channel 
        }

class Invitec(Command):
    def __init__(self, channel : str, handle : str):
        self.channel = channel
        self.handle = handle
        Command.__init__(self, "invitec")

    def get_payload(self):
        return {
            "command": "invitec",
            "channel": self.channel,
            "handle": self.handle
        }

class Acceptc(Command):
    def __init__(self, channel : str):
        self.channel = channel
        Command.__init__(self, "acceptc")

    def get_payload(self):
        return {
            "command": "acceptc",
            "channel": self.channel,
        }

class Declinec(Command):
    def __init__(self, channel : str):
        self.channel = channel
        Command.__init__(self, "declinec")

    def get_payload(self):
        return {
            "command": "declinec",
            "channel": self.channel,
        }

class Msgch(Command):
    def __init__(self, channel: str, message: str):
        self.channel = channel 
        self.message = message

    def get_payload(self):
        return {
            "command": "msgch",
            "channel": self.channel,
            "message": self.message
        }

class Promote(Command):
    def __init__(self, channel: str, handle:str):
        self.channel = channel 
        self.handle = handle 
    
    def get_payload(self):
        return {
            "command": "promote",
            "channel": self.channel,
            "handle": self.handle
        }

class Demote(Command):
    def __init__(self, channel: str, handle:str):
        self.channel = channel 
        self.handle = handle 
    
    def get_payload(self):
        return {
            "command": "demote",
            "channel": self.channel,
            "handle": self.handle
        }

class Kick(Command):
    def __init__(self, channel: str, handle:str):
        self.channel = channel 
        self.handle = handle 
    
    def get_payload(self):
        return {
            "command": "kick",
            "channel": self.channel,
            "handle": self.handle
        }


class Leavec(Command):
    def __init__(self, channel: str):
        self.channel = channel 
    
    def get_payload(self):
        return {
            "command": "leavec",
            "channel": self.channel,
        }

class Deletec(Command):
    def __init__(self, channel: str):
        self.channel = channel 
    
    def get_payload(self):
        return {
            "command": "deletec",
            "channel": self.channel,
        }

class Block(Command):
    def __init__(self, handle : str):
        self.handle = handle 

    def get_payload(self): 
        return {
            "command": "block",
            "handle": self.handle
        }

class Unblock(Command):
    def __init__(self, handle : str):
        self.handle = handle 

    def get_payload(self): 
        return {
            "command": "unblock",
            "handle": self.handle
        }