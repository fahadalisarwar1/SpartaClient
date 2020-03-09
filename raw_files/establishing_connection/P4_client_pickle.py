import socket
import pickle

HEADER_SIZE = 10

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = ("192.168.0.16", 8080)
    s.connect(address)

    while True:
        packet = b''
        arriving = True
        while True:
            chunk = s.recv(12)

            if arriving:
                print("[+] New chunk length :", chunk[:HEADER_SIZE])
                chunk_len = int(chunk[:HEADER_SIZE])
                arriving = False
            print(f'[+] Full chunk length: {chunk_len}')
            packet += chunk
            print(len(packet))
            if len(packet)-HEADER_SIZE == chunk_len:
                print("[+] Full packet received")
                print(packet[HEADER_SIZE:])
                print(pickle.loads(packet[HEADER_SIZE:]))
                arriving = True
                packet = b''