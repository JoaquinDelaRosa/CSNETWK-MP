from ServerSocket import *

def main(): 
    socket = ServerSocket()    
    print("Server is running")
    
    socket.listen()

if __name__ == "__main__":
    main()