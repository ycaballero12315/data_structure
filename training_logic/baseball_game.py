from typing import List

class Pelotero:
    def __init__(self, nombre: str, 
                 cant_series: int, vb: int,
                 c_jit: int) -> None:
        self.nombre = nombre
        self.cant_series = cant_series
        self.vb = vb
        self.c_jit = c_jit
    
    def average(self) -> float:
        return (self.vb * 1000)/self.c_jit if self.c_jit != 0 else 0.0
    
class Equipo:
    def __init__(self):
        self.list_peloteros: List[Pelotero] = []
        
    def add_pelotero(self, pelotero:Pelotero) -> None:
        self.list_peloteros.append(pelotero)
        
    def avg_colectivo(self)-> float:
        if not self.list_peloteros:
            return 0.0
        total = sum(p.average() for p in self.list_peloteros)
        return total/len(self.list_peloteros)
    
    def ordenar_peloteros(self, cantidad: int)-> list:
       cantidad = min(cantidad, len(self.list_peloteros))
       return [(p.nombre, p.cant_series) for p in sorted(self.list_peloteros, key=lambda p:p.cant_series, reverse=True)[:cantidad]]
        
if __name__ == "__main__":
    p = Pelotero("yoeny",20,30,10)
    p1 = Pelotero('Alex',12,15,10)
    e = Equipo()
    e.add_pelotero(p)
    e.add_pelotero(p1)
    print(f'Average promedio: {e.avg_colectivo()}')
    print(f'peloteros por la cantidad de series: {e.ordenar_peloteros(2)}')

        
            