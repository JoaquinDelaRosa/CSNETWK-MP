from CommandHandler import *
from InputHandler import *
from Logger import * 

def main(): 
    print("CSNETWK MP v0.1")
    logger = Logger()
    input_handler = InputHandler(logger=logger)
    command_handler = CommandHandler()

    while(True):
        command = input("Command: ")
        result : Command = input_handler.parse(command)
        

if __name__ == "__main__":
    main()