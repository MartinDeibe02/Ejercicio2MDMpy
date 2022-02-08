from abc import ABC, abstractmethod


class Moneda(ABC):
    def __init__(self,cantidad):
        self.cantidad=cantidad

    def cantidadEnEuros(self):
        pass

@abstractmethod
class Dolar(Moneda):
    def cantidadEnEuros(self):
        return self.cantidad*0.89

@abstractmethod
class Yen(Moneda):
    def cantidadEnEuros(self):
        return self.cantidad * 0.0078

@abstractmethod
class Libra(Moneda):
    def cantidadEnEuros(self):
        return self.cantidad * 1.20

