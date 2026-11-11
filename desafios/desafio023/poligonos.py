import math
from abc import ABC, abstractmethod


class Poligono(ABC):

    def __init__(self, lados):
        self.qtd_lados = lados

    @abstractmethod
    def perimetro(self) -> float:
        pass

    @abstractmethod
    def area(self) -> float:
        pass

class Quadrado(Poligono):

    def __init__(self, lado = 1):
        super().__init__(4)
        self.lado = lado