from core.connection.connection import *
from core.connection.handler import  *

if __name__ == "__main__":
    my_socket = ClientConnection()

    my_socket.Connect("192.168.0.16", 8080)
    handleConnection(my_socket)
    print("[+] Connected ")

    my_socket.Close()