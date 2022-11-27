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
    def __init__(self, channel_name : str):
        self.channel_name = channel_name
        Command.__init__(self, "createc")

    def get_payload(self):
        return {
            "command": "createc",
            "channel": self.channel_name 
        }

class Invitec(Command):
    def __init__(self, channel_name : str, handle : str):
        self.channel_name = channel_name
        self.handle = handle
        Command.__init__(self, "invitec")

    def get_payload(self):
        return {
            "command": "invitec",
            "channel": self.channel_name,
            "handle": self.handle
        }