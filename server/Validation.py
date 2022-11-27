from Response import *

def make_bad_form_response(key : str , sender_addr : tuple):
    return [Response("Error: Received object is in bad form. Expecting '" + key +"' as a keyword", [sender_addr])]

def make_unknown_sender(sender_addr: tuple):
    return [Response("Error: Unknwon sender. Please join or register first.", [sender_addr])]

def make_handle_not_found(sender_addr: tuple):
    return [Response("Error: Handle or alias not found.", [sender_addr])]

def make_channel_not_found(sender_addr : tuple):
    return [Response("Error: Channel not found.", [sender_addr])]

def make_failed_permissions(sender_addr: tuple):
    return [Response("Error: You do not have permission to do this", [sender_addr])]