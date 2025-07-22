from typing import List

class Animal_Exo:
    def __init__(self, tipo: str, 
                 nombre: str):
        self.tipo = tipo
        self.nombre = nombre

class Jaula:
    def __init__(self, numero: int, 
                 animal: Animal_Exo, cantidad: int):
        self.numero = numero
        self.animal = animal
        self.cantidad = cantidad
    
class Exposicion:
    def __init__(self):
        self.jaulas: List[Jaula] = []
    
    def add_jaula(self, jaula: Jaula) -> None:
        if len(self.jaulas)< 25:
            self.jaulas.append(jaula)
    
    def organizar_jaula(self)-> List[Jaula]:
        return [j.numero for j in sorted(self.jaulas, key=lambda j : j.cantidad)]
    
    def buscar_animal_tipo(self, tipo: str) -> int:
        for j in self.jaulas:
            if j.animal.tipo == tipo:
                return j.numero
        return -1
    
    def jaula_menor_cant_animales(self) -> int:
        return min(self.jaulas,key=lambda j : j.cantidad).numero
    
    def contar_jaulas_con_mas_de(self, cant_min:int)->int:
        return sum(1 for j in self.jaulas if j.cantidad > cant_min)
    
    def avg_animales_x_jaulas(self) -> float:
        filtro = [j.cantidad for j in self.jaulas if j.cantidad < 10]
        if not filtro:
            return 0.0
        total = sum(j.cantidad for j in filtro)
        return total/len(filtro)
        
if __name__ == "__main__":
    animal1 = Animal_Exo('ave', 'perico')
    animal2 = Animal_Exo('ave', 'sorsal')
    
    jaula1 = Jaula(1,animal1,2)
    exp = Exposicion()
    exp.add_jaula(jaula1)
    for j in exp.organizar_jaula():
        print(j)
    
    
    