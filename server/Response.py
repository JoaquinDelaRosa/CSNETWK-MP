
class Response: 
    def __init__(self, message : str, targets : list[tuple]):
        self.message = message
        self.targets =targets
    
    def __dict__(self) -> dict:
        return {
            'message' : self.message
        }

    def __bytes__(self):
        return str(self.__dict__()).encode()
    
    def get_targets(self):
        return self.targets