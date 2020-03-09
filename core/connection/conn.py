import socket


def ConnectWithServer(ip="192.168.0.16", port=8080):
    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    skt.connect((ip, port))
    print("[+] Connected with ", ip)
    return skt

def send_data(skt, data):
    data_in_bytes = bytes(data, "utf-8")
    skt.send(data_in_bytes)


def receive_data(skt):
    data_in_bytes = skt.recv(1024)
    data = data_in_bytes.decode("utf-8")
    return data
