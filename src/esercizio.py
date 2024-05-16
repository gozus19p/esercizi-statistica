from typing import Generic, TypeVar
from abc import ABC, abstractmethod

Out = TypeVar("Out")


class Esercizio(Generic[Out], ABC):
    def __init__(self, consegna: str):
        self.nome = self.__class__.__name__
        self.consegna = consegna

    @abstractmethod
    def execute(self) -> Out:
        pass
