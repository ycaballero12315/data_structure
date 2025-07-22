from typing import List

class Atleta:
    
    def __init__(self, nombre: str,
                 sexo: str, registro: float):
        self.nombre = nombre
        self.sexo = sexo
        self.registro = registro
        
class Evento_Natacion:
    def __init__(self):
        self.nadadores: List[Atleta] = []
    
    def add_nadador(self, n: Atleta)->None:
        self.nadadores.append(n)
    
    def nadador_romp_record(self, record_n: float) -> str:
        filtrar_genero = [n for n in self.nadadores if n.registro > record_n and n.sexo == 'm']
        if not filtrar_genero:
            return 0.0
        return max(filtrar_genero, key=lambda n : n.registro).nombre
    
    def order_nadador_record(self) -> None:
        ordenados =  sorted(self.nadadores, key=lambda n : n.registro, reverse=True)
        return [n.nombre for n in ordenados]
    
    def count_nadadores_superaron_tiempo(self, tiempo) -> int:
        return sum(1 for n in self.nadadores if n.registro > tiempo)
    
    def nadador_menos_rendimiento(self)->str:
        return min(self.nadadores, key=lambda n : n.registro).nombre
    
    def nadador_mayor_rendimiento(self)->str:
        return max(self.nadadores, key=lambda n : n.registro).nombre
    