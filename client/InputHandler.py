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

        # Additional commands
        if command == "/channels":
            return self.__parse_channels_command__(toks)
        if command == "/createc":
            return self.__parse_createc_command__(toks)
        if command == "/invitec":
            return self.__parse_invitec_command__(toks)
        if command == "/acceptc":
            return self.__parse_acceptc_command__(toks)
        if command == "/declinec":
            return self.__parse_declinec_command__(toks)
        if command == "/msgch":
            return self.__parse_msgch_command__(toks)
        if command == "/promote":
            return self.__parse_promote_command__(toks)
        if command == "/demote":
            return self.__parse_demote_command__(toks)
        if command == "/leavec":
            return self.__parse_leavec_command__(toks)
        if command == "/kick":
            return self.__parse_kick_command__(toks)
        if command == "/deletec":
            return self.__parse_deletec_command__(toks)
        if command == "/list":
            return self.__parse_list_command__(toks)
        if command == "/listch":
            return self.__parse_listch_command__(toks)
        if command == "/listblk":
            return self.__parse_listblk_command__(toks)
        if command == "/block":
            return self.__parse_block_command__(toks)
        if command == "/unblock":
            return self.__parse_unblock_command__(toks)

        return self.__handle_command_not_found_error__()
    
    def __handle_command_not_found_error__(self):
        self.logger.log("Error: Command Not Found.")
        return None
        
    def __handle_bad_syntax_error__(self):
        self.logger.log("Command parameters do not match or is not allowed.")
        return None

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
            | /channels                    | Display a list of all the   |
            |                              | channels in the server      |
            +------------------------------+-----------------------------+
            | /createc <channel>           | Create a channel in the     |
            |                              | server if it doesn't exist. |
            |                              | You become the owner.       |
            +------------------------------+-----------------------------+
            | /invitec <channel> <handle>  | Invite a user to the        |
            |                              | channel if they are not     |
            |                              | yet a member                |
            +------------------------------+-----------------------------+
            | /acceptc <channel>           | Acceot an invitation        |
            |                              | to a channel                |
            +------------------------------+-----------------------------+
            | /declinec <channel>          | Decline an invitation       |
            |                              | to a channel                |
            +------------------------------+-----------------------------+
            | /msgch <channel>             | Send a message to all       |
            |                              | members in a channel        |
            +------------------------------+-----------------------------+
            | /promote <channel> <handle>  | Requires admin perms:       |
            |                              | promote channel member to   |
            |                              | admin                       |
            +------------------------------+-----------------------------+
            | /demote <channel> <handle>   | Requires admin perms:       |
            |                              | demote channel admin   to   |
            |                              | member                      |
            +------------------------------+-----------------------------+
            | /leavec <channel>            | If you are not the owner    |
            |                              | leave the channel           |
            +------------------------------+-----------------------------+
            | /kick <channel> <handle>     | Requires admin perms:       |
            |                              | kick a channel member       |
            +------------------------------+-----------------------------+
            | /deletec <channel>           | Requires owner perms:       |
            |                              | delete a channel            |
            +------------------------------+-----------------------------+
            | /block <handle>              | BLock a user. You will not  |
            |                              | receive any messages from   |
            |                              | them                        |
            +------------------------------+-----------------------------+
            | /unblock <handle>            | UnbLock a user. You will    |
            |                              | receive messages from them  |
            +------------------------------+-----------------------------+
            | /?                           | Request command help        |
            +------------------------------+-----------------------------+
            
        """)
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

    def __parse_channels_command__(self, toks: list):
        if len(toks) != 1:
            return self.__handle_bad_syntax_error__()
        
        return Channels()
    
    def __parse_createc_command__(self, toks: list):
        if len(toks) != 2:
            return self.__handle_bad_syntax_error__()
        
        channel = toks[1]
        if len(channel) == 0:
            return self.__handle_bad_syntax_error__()
        
        return Createc(channel)

    def __parse_invitec_command__(self, toks: list):
        if len(toks) != 3:
            return self.__handle_bad_syntax_error__()
        
        channel = toks[1]
        handle = toks[2]

        return Invitec(channel, handle)

    def __parse_acceptc_command__(self, toks: list):
        if len(toks) != 2:
            return self.__handle_bad_syntax_error__()
        
        channel = toks[1]

        return Acceptc(channel)
    
    def __parse_declinec_command__(self, toks: list):
        if len(toks) != 2:
            return self.__handle_bad_syntax_error__()
        
        channel = toks[1]

        return Declinec(channel)

    def __parse_msgch_command__(self, toks : list):
        if len(toks) < 3:
            return self.__handle_bad_syntax_error__() 

        channel = toks[1]
        message = ' '.join(toks[2:])

        if len(channel) == 0 or len(message) == 0:
            return self.__handle_bad_syntax_error__()

        return Msgch(channel, message)

    def __parse_promote_command__(self, toks :list):
        if len(toks) != 3: 
            return self.__handle_bad_syntax_error__()

        channel = toks[1]
        handle = toks[2]

        if len(channel) == 0 or len(handle) == 0:
            return self.__handle_bad_syntax_error__
        
        return Promote(channel, handle)
    
    def __parse_demote_command__(self, toks :list):
        if len(toks) != 3: 
            return self.__handle_bad_syntax_error__()

        channel = toks[1]
        handle = toks[2]

        if len(channel) == 0 or len(handle) == 0:
            return self.__handle_bad_syntax_error__()
        
        return Demote(channel, handle)

    def __parse_leavec_command__(self, toks :list):
        if len(toks) != 2: 
            return self.__handle_bad_syntax_error__()

        channel = toks[1]

        if len(channel) == 0:
            return self.__handle_bad_syntax_error__()
        
        return Leavec(channel)
    
    def __parse_kick_command__(self, toks :list):
        if len(toks) != 3: 
            return self.__handle_bad_syntax_error__()

        channel = toks[1]
        handle = toks[2]

        if len(channel) == 0 or len(handle) == 0:
            return self.__handle_bad_syntax_error__()
        
        return Kick(channel, handle)
    
    def __parse_deletec_command__(self, toks :list):
        if len(toks) != 2: 
            return self.__handle_bad_syntax_error__()

        channel = toks[1]

        if len(channel) == 0:
            return self.__handle_bad_syntax_error__()
        
        return Deletec(channel) 
    
    def __parse_list_command__(self, toks: list):
        if len(toks) != 1:
            return self.__handle_bad_syntax_error__()
        
        return List()

    def __parse_listch_command__(self, toks: list):
        if len(toks) != 2:
            return self.__handle_bad_syntax_error__()
        
        channel = toks[1]
        if len(channel) == 0:
            return self.__handle_bad_syntax_error__()

        return Listch(channel)

    def __parse_listblk_command__(self, toks: list):
        if len(toks) != 1:
            return self.__handle_bad_syntax_error__()
        
        return Listblk() 

    def __parse_block_command__(self, toks : list):
        if len(toks) != 2:
            return self.__handle_bad_syntax_error__()
        
        handle = toks[1]

        if len(handle) == 0:
            return self.__handle_bad_syntax_error__()

        return Block(handle)

    def __parse_unblock_command__(self, toks : list):
        if len(toks) != 2:
            return self.__handle_bad_syntax_error__()
        
        handle = toks[1]

        if len(handle) == 0:
            return self.__handle_bad_syntax_error__()

        return Unblock(handle)
    