import socket
import pickle
import os
import tempfile
from cryptography.fernet import Fernet

HEADER_SIZE = 10


CHUNK_SIZE = 4 * 1024
END_DELIMETER = "*END_OF_FILE*"
COMMAND_DELIMETER = "<END_OF_COMMAND>"


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

    def receive_file(self):
        tmp = tempfile.gettempdir()
        file_name = self.receive_data()

        path_dir, actual_file_name = os.path.split(file_name)

        temp_path = os.path.join(tmp, actual_file_name)
        with open(temp_path, "wb") as file:
            while True:
                chunk = self.socket.recv(CHUNK_SIZE)

                if chunk.endswith(END_DELIMETER.encode()):

                    chunk = chunk[:-len(END_DELIMETER)]

                    file.write(chunk)
                    print("[+] Completed Transfer")
                    break

                if "NOT_FOUND".encode() in chunk:
                    print("[-] Unable to locate file")
                    break
                file.write(chunk)


    def send_command_result(self, command_result):
        print("[+] Sending Command Result")
        chunk = command_result + COMMAND_DELIMETER
        chunk_bytes = chunk.encode()

        self.socket.sendall(chunk_bytes)



    def Close(self):
        self.socket.close()



