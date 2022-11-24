from client.InputHandler import *

def main(): 
    print("CSNETWK MP v0.1")
    inputHandler = InputHandler()

    while(True):
        command = input("Command: ")
        result : InputResult = inputHandler.parse(command)
        print(str(result))

if __name__ == "__main__":
    main()