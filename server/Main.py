from Configs import *
from ServerSocket import *


def main(): 
    socket = ServerSocket()    
    print("Server is running at address " + IP_ADDRESS + " port=" + str(PORT_NUMBER))
    
    socket.listen()

if __name__ == "__main__":
    main()



