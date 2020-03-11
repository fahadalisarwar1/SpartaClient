import socket
import pickle
import os


HEADER_SIZE = 10


CHUNK_SIZE = 4 * 1024
END_DELIMETER = "*END_OF_FILE*"


class ClientConnection:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def Connect(self, server_ip, server_port):
        self.socket.connect((server_ip, server_port))
        self.server_ip = server_ip
        self.server_port = server_port

    def receive_data(self):
        self.data_in_bytes = self.socket.recv(1024)
        self.data = self.data_in_bytes.decode("utf-8")
        return self.data

    def send_data(self, data):
        self.data_in_bytes = bytes(data, "utf-8")
        self.socket.send(self.data_in_bytes)

    def send_serialized(self, data):

        cmd_dict = {"cmd_ouput": data}

        pickled_data = pickle.dumps(cmd_dict)

        self.data_in_bytes = bytes(f"{len(pickled_data):<{HEADER_SIZE}}", 'utf-8') + pickled_data
        self.socket.send(self.data_in_bytes)

    def receive_data_bytes(self):
        print("[+] Receiving Files")
        with open("image.jpeg") as file:
            while True:
                data = self.socket.recv(1024)
                if not data:
                    break
                file.write(data)
            print("[+] Successfully downloaded the file")

    def receive_file(self):
        file_name = self.receive_data()
        print(file_name)
        path_dir, actual_file_name = os.path.split(file_name)
        print("actual :", actual_file_name)
        with open(actual_file_name, "wb") as file:
            while True:
                bits = self.socket.recv(CHUNK_SIZE)
                if bits.endswith(END_DELIMETER.encode()):
                    file.write(bits[:-len(END_DELIMETER)])
                    print("[+] Completed Transfer")
                    break
                if "NOT_FOUND".encode() in bits:
                    print("[-] Unable to locate file")
                    break
                file.write(bits)





    def Close(self):
        self.socket.close()