

def run_command(my_socket):
    print("[+] Running System Command ")

    keep_running = True
    while keep_running:
        command = my_socket.receive_data()
        print("Entered Command is : ", command)
        if command == "stop" or command == "exit":
            keep_running = False
            command_result = "[-] Exiting"

        else:
            command_result = "[+] This is the command result"
        my_socket.send_data(command_result)

