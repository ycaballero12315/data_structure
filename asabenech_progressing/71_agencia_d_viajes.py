from typing import List, Tuple, Dict, TypedDict

class DTViaje(TypedDict):
    destino: str
    list_lugares: List[Tuple[str,str]]
    descripcion: str
    
class Viaje:
    
    def __init__(self):
        self.viajes: Dict[str,DTViaje] = {}
    
    def add_elem(self, destino:str, 
                 list_lugares:List[Tuple[str,str]], 
                 descripcion:str)->None:
        """
        Agrega un nuevo viaje al registro.
        """
        num_viaje = f"viaje_{len(self.viajes)+1}"
        self.viajes[num_viaje] = DTViaje(
                destino = destino,
                list_lugares = list_lugares,
                descripcion = descripcion
            )
        
    def obtener_viaje(self)->Dict[str,DTViaje]:
        """
        Devuelve todos los viajes registrados.
        """
        return self.viajes

def mostrar_viaje(viajes_d: Dict[str,DTViaje])->None:
    if not viajes_d:
        print("no existe registro de viajes: ")
        return
    
    for num_viaje, detalles in viajes_d.items():
        print("--Viajes--")
        print(f"Numero de Viaje: {num_viaje}:\n ")
        print(f"Destino->{detalles['destino']}\n")
        print("___"*10 + '\n')
        print("Lugares Visitados \n")
        for lugar, fecha in detalles["list_lugares"]:
            print(f"lugar: {lugar}, fecha: {fecha}")
        print("\n")
        print(f"Descripcion del viaje: {detalles["descripcion"]}")

def main():
    registro_viaje = Viaje()
    registro_viaje.add_elem(
        destino="París",
        list_lugares=[("Torre Eiffel", "2025-01-15"), ("Museo del Louvre", "2025-01-16")],
        descripcion="Un viaje inolvidable a la ciudad del amor.") 
    
    registro_viaje.add_elem(
        destino="Nueva York",
        list_lugares=[("Times Square", "2025-02-10"), ("Central Park", "2025-02-11")],
        descripcion="Explorando la gran manzana.")  
    
    mostrar_viaje(registro_viaje.obtener_viaje())     

if __name__ == "__main__":
    main()