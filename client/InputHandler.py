from Command import *
from Logger import *
from Utils import *


class InputHandler: 
    def __init__(self, logger : Logger):
        self.logger = logger
    
    def parse(self, str : str):
        str = str.strip()
        toks = str.split(' ')
        if (len(toks) == 0):
            return self.__handle_command_not_found_error__()

        command = toks[0]
        if command == "/join":
            return self.__parse_join_command__(toks)
        if command == "/leave":
            return self.__parse_leave_command__(toks)
        if command == "/register":
            return self.__parse_register_command__(toks)
        if command == "/all":
            return self.__parse_all_command__(toks)
        if command == "/msg":
            return self.__parse_msg_command__(toks)
        if command == "/?":
            return self.__parse_help_command__(toks)

        return self.__handle_command_not_found_error__()
    
    def __handle_command_not_found_error__(self):
        self.logger.log("Error: Command Not Found.")
        return None
        
    def __handle_bad_syntax_error__(self):
        self.logger.log("Command parameters do not match or is not allowed.")
        return None

    def __parse_join_command__(self, toks : list):
        if len(toks) != 3:
            return self.__handle_bad_syntax_error__()
        
        server_ip_address = toks[1]
        port = toks[2]

        if (not is_valid_ip_address(server_ip_address) or not(port.isdigit())):
            return self.__handle_bad_syntax_error__()

        return Join(server_ip_address=server_ip_address, port=int(port))

    def __parse_leave_command__(self, toks : list):
        if len(toks) != 1:
            return self.__handle_bad_syntax_error__()
        
        return Leave()
    
    def __parse_register_command__(self, toks : list):
        if len(toks) != 2:
            return self.__handle_bad_syntax_error__()

        handle = toks[1]
        if len(handle) == 0:
            return self.__handle_bad_syntax_error__()

        return Register(handle=handle)

    def __parse_all_command__(self, toks: list):
        if len(toks) < 2:
            return self.__handle_bad_syntax_error__() 

        message = ' '.join(toks[1:])

        if len(message) == 0:
            return self.__handle_bad_syntax_error__()

        return All(message)

    def __parse_msg_command__(self, toks: list):
        if len(toks) < 3:
            return self.__handle_bad_syntax_error__() 

        handle = toks[1]
        message = ' '.join(toks[2:])

        if len(handle) == 0 or len(message) == 0:
            return self.__handle_bad_syntax_error__()

        return Msg(handle, message)

    def __parse_help_command__(self, toks: list):
        if len(toks) != 1:
            return self.__handle_bad_syntax_error__()

        self.logger.log("""
            +------------------------------+-----------------------------+
            | Input Syntax                 | Description                 |
            +------------------------------+-----------------------------+
            | /join <server_ip_add> <port> | Connect to the server       |
            |                              | application                 |
            +------------------------------+-----------------------------+
            | /leave                       | Disconnect from the server  |
            |                              | application                 |
            +------------------------------+-----------------------------+
            | /register <handle>           | Register a unique handle    |
            |                              | or alias                    |
            +------------------------------+-----------------------------+
            | /all <message>               | Send message to all         |
            +------------------------------+-----------------------------+
            | /msg <handle> <message>      | Send direct message to a    |
            |                              | single handle               |
            +------------------------------+-----------------------------+
            | /?                           | Request command help        |
            +------------------------------+-----------------------------+
        """)
        return None