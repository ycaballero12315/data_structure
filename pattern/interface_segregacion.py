from abc import ABC, abstractmethod

'''Solo implementar en las clases los metodos que se van a usar'''


class Trabajar(ABC):
    @abstractmethod
    def trabajador(self):
        pass
    

class Comer(ABC):
    @abstractmethod
    def comer(self):
        pass


class Persona(Trabajar, Comer):
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def trabajador(self):
        return f'El trabajador {self.name} trabaja mucho'
    
    def comer(self):
        return f"Come mucho {self.name}"
    

class Robot(Trabajar):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def trabajador(self):
        return f'El robot {self.name} trabaja mucho'

class Ninno(Trabajar, Comer):
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def trabajador(self):
        return f'El niño {self.name} juega mucho'
    
    def comer(self):
        return f"Come dulces {self.name}"
    
