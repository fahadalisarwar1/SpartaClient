from core.connection.conn import *


def run_command(socket):
    print("[+] Running System Command ")
    command = receive_data(socket)
    print("Entered Command is : ", command)