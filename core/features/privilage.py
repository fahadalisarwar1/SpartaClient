import ctypes, sys
from elevate import elevate

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def try_UAC_bypass(my_socket):
    if is_admin():
        # Code of your program here
        print("[+] It is already in admin mode")


    else:
        # Re-run the program with admin rights
        print("[-] Trying to escalate to ADMIN")
        elevate(show_console=False)


import sys
import ctypes


def run_as_admin(argv=None, debug=False):
    shell32 = ctypes.windll.shell32
    if argv is None and shell32.IsUserAnAdmin():
        return True

    if argv is None:
        argv = sys.argv
    if hasattr(sys, '_MEIPASS'):
        # Support pyinstaller wrapped program.
        arguments = map(str, argv[1:])
    else:
        arguments = map(str, argv)
    argument_line = u' '.join(arguments)
    executable = str(sys.executable)
    if debug:
        print
        'Command line: ', executable, argument_line
    ret = shell32.ShellExecuteW(None, u"runas", executable, argument_line, None, 1)
    if int(ret) <= 32:
        return False
    return None


def try_elevating():
    ret = run_as_admin()
    if ret is True:
        print('I have admin privilege.')
        #raw_input('Press ENTER to exit.')
    elif ret is None:
        print('I am elevating to admin privilege.')
        #raw_input('Press ENTER to exit.')
    else:
        print('Error(ret=%d): cannot elevate privilege.' % (ret,))
