from typing import Literal, Any
from colorama import Fore, init

from ....Domain.ports.custom_print import CustomPrint, CustomPrintData

init(autoreset=True)

class ColoramaCustomPrinter(CustomPrint):

    def print(self, data: CustomPrintData):
        print(Fore.CYAN + "-------------------------------------------------")
        if data.status == "warning":
            print(Fore.YELLOW + str(data.message))
        if data.status == "error":
            print(Fore.RED + str(data.message))
        elif data.status == "success":
            print(Fore.GREEN + str(data.message))
        elif data.status == "normal":
            print(str(data.message))