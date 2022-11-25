class Command: 
    command: str

    def __init__(self, command: str):
        self.command = command

class Join(Command):

    def __init__(self, server_ip_address, port):
        self.server_ip_address = server_ip_address
        self.port =port
        Command.__init__(self, "join")

class Leave(Command):

    def __init__(self):
        Command.__init__(self, "leave")

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