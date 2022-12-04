import threading

from ClientSocket import *
from CommandHandler import *
from InputHandler import *
from Logger import * 

def input_thread(client_socket: ClientSocket):
    print("CSNETWK MP v1.0")
    logger = Logger()
    input_handler = InputHandler(logger=logger)
    command_handler = CommandHandler(logger=logger, client_socket=client_socket)

    while True:
        command = input()
        result : Command = input_handler.parse(command)
        command_handler.process(result)



def main(): 
    logger = Logger()
    socket = ClientSocket(logger)
    t1 = threading.Thread(target=input_thread, args=(socket,))
    t1.start()

    t1.join()

if __name__ == "__main__":
    main()