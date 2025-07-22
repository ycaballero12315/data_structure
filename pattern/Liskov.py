from abc import ABC, abstractmethod


class Perro(ABC):
    @abstractmethod
    def sonido(self, murmullo):
        pass


class PerroReal(Perro):
    def sonido(self, murmullo):
        return f'El perro hace {murmullo}'


class PerroGoma(Perro):
    def sonido(self, murmullo):
        return f'El perro no real hace {murmullo}'