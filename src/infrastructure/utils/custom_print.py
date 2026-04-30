from typing import Literal, Any

from colorama import Fore, Style, init

init(autoreset=True)

def print_c(status:Literal["error","success","normal"], message:Any):
    if status == "error":
        print(Fore.RED + str(message))
    elif status == "success":
        print(Fore.GREEN + str(message))
    elif status == "normal":
        print(str(message))