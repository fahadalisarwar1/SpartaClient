import socket
import core.connection.conn as conn

if __name__ == "__main__":

    skt = conn.ConnectWithServer("192.168.0.16", 8080)
    print("[+] " + conn.receive_data(skt))
    conn.send_data(skt, "Hello i am the the client")
    skt.close()