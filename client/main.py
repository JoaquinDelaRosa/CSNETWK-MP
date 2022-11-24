from CommandHandler import *
from InputHandler import *
from Logger import * 

def main(): 
    print("CSNETWK MP v0.1")
    logger = Logger()
    input_handler = InputHandler(logger=logger)
    command_handler = CommandHandler(logger=logger)

    while(True):
        command = input("Command: ")
        result : Command = input_handler.parse(command)
        command_handler.process(result)
        

if __name__ == "__main__":
    main()