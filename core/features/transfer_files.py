

def download_files(my_socket):
    print("[+] Downloading files")
    my_socket.receive_file()


def upload_files(my_socket):
    print("[+] Uploading files")
    my_socket.send_file()