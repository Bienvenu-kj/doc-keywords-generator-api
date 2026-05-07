from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Literal


@dataclass
class CustomPrintData:
    status: Literal["error", "success", "normal", "warning"]
    message: Any

class CustomPrint(ABC):
    @abstractmethod
    def print(self, data:CustomPrintData) -> None:
        pass