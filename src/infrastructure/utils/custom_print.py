from typing import Literal

from colorama import Fore, Style, init

init(autoreset=True)

def print_c(status:Literal["error","success","normal"], message:str):
    if status == "error":
        print(Fore.RED + message)
    elif status == "success":
        print(Fore.GREEN + message)
    elif status == "normal":
        print(message)