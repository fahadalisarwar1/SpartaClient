import socket

HEADER_SIZE = 10

if __name__ == "__main__":
    serverIP = "192.168.0.16"
    server_port = 8081

    address = (serverIP, server_port)

    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(address)
    print("[+] connection established with server ", serverIP)
    while True:
        full_msg = ""
        new_msg = True
        while True:
            msg = conn.recv(16)
            if new_msg:
                print(f'new message len : {msg[:HEADER_SIZE]}')
                msg_len = int(msg[:HEADER_SIZE])
                new_msg = False

            full_msg += msg.decode("utf-8")
            if len(full_msg)-HEADER_SIZE == msg_len:
                print("full message received")
                print(full_msg[HEADER_SIZE:])
                new_msg =True
                full_msg = ""
        print(full_msg)

