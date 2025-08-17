from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sonido(self, murmullo):
        pass


class PerroReal(Animal):
    def sonido(self, murmullo):
        return f'El perro hace {murmullo}'


class PerroGoma(Animal):
    def sonido(self, murmullo):
        return f'El perro no real hace {murmullo}'

class GatoReal(Animal):
    def sonido(self, murmullo):
        return f'El gato hace {murmullo}'