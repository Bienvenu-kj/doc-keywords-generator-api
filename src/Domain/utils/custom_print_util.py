from ..ports.custom_print import CustomPrintData
from ...Domain.ports.custom_print import CustomPrint


class CustomPrintUtil:
    def __init__(self, custom_print: CustomPrint, data:CustomPrintData) -> None:
        self.custom_print = custom_print
        self.data = data

    def print(self) -> None:
        self.custom_print.print(self.data)
