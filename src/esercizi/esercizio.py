from typing import Generic, TypeVar
from abc import ABC, abstractmethod

Out = TypeVar("Out")


class Esercizio(Generic[Out], ABC):
    def __init__(self, nome: str, consegna: str):
        self.nome = nome
        self.consegna = consegna

    @abstractmethod
    def execute(self) -> Out:
        pass
