import socket


if __name__ == "__main__":
    serverIP = "192.168.0.22"
    server_port = 8080

    address = (serverIP, server_port)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



