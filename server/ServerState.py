class ServerState:
    handles: dict = {}

    def try_register_handle(self, handle : str) -> bool:
        if self.is_recognized_handle(handle):
            return False 

        self.handles[handle] = {}            
        return True
    
    def is_recognized_handle(self, handle: str) -> bool:
        p_handle = handle.lower()
        if len(p_handle) == 0:
            return False 
        
        return p_handle in self.handles
    
