from abc import ABC, abstractmethod


class Descuento(ABC):
    @abstractmethod
    def calcular(self, saldo: float):
        pass


class DescuentoFijo(Descuento):
    def calcular(self, saldo):
        return saldo - 100


class DescuentoPorCiento(Descuento):
    def calcular(self, saldo, descuento):
        return saldo * descuento
    
Descuento = DescuentoPorCiento()
print(Descuento.calcular(1000, 0.1))