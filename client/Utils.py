import ast 

def is_valid_ip_address(ip : str) -> bool :
    octs = ip.split('.')
    if (len(octs) != 4):
        return False 

    for x in octs:
        if not x.isdigit():
            return False

        if int(x) > 255 or int(x) < 0:
            return False

    return True

def get_response_message(res : bytes ) -> str:
    decoded = ast.literal_eval(res.decode())
    if not "message" in decoded:
        return ""
    return decoded["message"]