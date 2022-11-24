from .InputResult import *
from .Utils import *

class InputHandler: 
    def __init__(self):
        pass 
    
    def parse(self, str : str):
        toks = str.split(' ')
        if (len(toks) == 0):
            return COMMAND_NOT_FOUND_ERROR

        command = toks[0]
        if (command == "/join"):
            return self.__parse_join_command__(toks)
        if (command == "/leave"):
            return self.__parse_leave_command__(toks)
        if (command == "/register"):
            return self.__parse_register_command__(toks)
        if (command == "/all"):
            return self.__parse_all_command__(toks)
        if (command == "/msg"):
            return self.__parse_msg_command__(toks)
        if (command == "/?"):
            return self.__parse_help_command__(toks)

        return COMMAND_NOT_FOUND_ERROR
    
    def __parse_join_command__(self, toks : list):
        if (len(toks) != 3):
            return COMMAND_BAD_SYNTAX_ERROR
        
        server_ip_address = toks[1]
        port = toks[2]

        if (not is_valid_ip_address(server_ip_address)):
            return COMMAND_BAD_SYNTAX_ERROR

        return InputResult( "" ,{
            "command": "join",
            "server_ip_address": server_ip_address,
            "port": port
        })

    def __parse_leave_command__(self, toks : list):
        if (len(toks) != 1):
            return COMMAND_BAD_SYNTAX_ERROR
        
        return InputResult("", {
            "command": "leave"
        })
    
    def __parse_register_command__(self, toks : list):
        if (len(toks) != 2):
            return COMMAND_BAD_SYNTAX_ERROR

        handle = toks[1]
        if (len(handle) == 0):
            return COMMAND_BAD_SYNTAX_ERROR

        return InputResult("", {
            "command": "register",
            "handle": handle
        })

    def __parse_all_command__(self, toks: list):
        if (len(toks) < 2):
            return COMMAND_BAD_SYNTAX_ERROR 

        message = ''.join(toks[1:])

        if (len(message) == 0):
            return COMMAND_BAD_SYNTAX_ERROR

        return InputResult("", {
            "command": "all",
            "message": message
        })

    def __parse_msg_command__(self, toks: list):
        if (len(toks) < 3):
            return COMMAND_BAD_SYNTAX_ERROR 

        handle = toks[1]
        message = ''.join(toks[2:])

        if (len(handle) == 0 or len(message) == 0):
            return COMMAND_BAD_SYNTAX_ERROR

        return InputResult("", {
            "command": "msg",
            "handle": handle,
            "message": message
        })

    def __parse_help_command__(self, toks: list):
        if (len(toks) != 1):
            return COMMAND_BAD_SYNTAX_ERROR

        return InputResult("""
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