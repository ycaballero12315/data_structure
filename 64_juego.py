from typing import List, Dict

class Juegos:
    def __init__(self):
        self.ptos_jugadores: Dict[str,List[float]] = {}
        
    def add_average(self, nombre: str, puntuacion: float) -> None:
        if nombre not in self.ptos_jugadores:
            self.ptos_jugadores[nombre] = []
        
        self.ptos_jugadores[nombre].append(puntuacion)
    
    def average(self, nombre: str)-> float:
        if nombre in self.ptos_jugadores and self.ptos_jugadores[nombre]:
            avg=sum(self.ptos_jugadores[nombre])/len(self.ptos_jugadores[nombre])
            return avg
        return 0.0
    
    def print_register(self)-> Dict[str,Dict[str, float]]:
        if not self.ptos_jugadores:
            raise ValueError("No existen jugadores registrados")
        return {
            nombre:{
                "puntuaciones": puntuaciones,
                "promedio":self.average(nombre)
            }
            for nombre, puntuaciones in self.ptos_jugadores.items()
        }

"""Validaciones"""
def validar_nombre(nombre: str)->str:
    if not nombre:
        raise ValueError("Error en el nombre ")
    nombre = nombre.strip().lower()
    return nombre

def validar_puntaje(puntaje: str)-> float:
    puntaje = float(puntaje)
    if not puntaje:
        raise ValueError("Debe insertar un puntaje")
    elif puntaje <= 0:
        raise ValueError("El puntaje tiene que ser mayor a cero.")
    return puntaje

"""Funcion global para mostrar registro"""
def mostrar_registro(jugador: Juegos)->None:
    registro = jugador.print_register()
    try:
      for nombre, data in registro.items():
          puntuaciones = data["puntuaciones"]
          promedio = data["promedio"]
          print(f"El jugador: {nombre} tiene una Puntuacion: {puntuaciones}, con un Promedio: {promedio}")
    except ValueError as e:
      print(f'Error occurred: {e}')
      
      
def main():
    jugador = Juegos()
    while True:
        try:
          continuar = input("Desea agregar mas jugadores?, (si/no): ")
          if continuar == "no":
              break
          
          nombre = validar_nombre(input("Nombre del jugador: "))
          puntaje = validar_puntaje(input("Inserte los ptos del juego: "))
          jugador.add_average(nombre,puntaje)
          
          mostrar_registro(jugador)
          
          option = input("Desea continuar agregando ptos a los jugadores (s/n)").lower().strip()
          if option != "s":
                break 
          
        except ValueError as e:
          print(f'Error occurred: {e}')
    
    try:
        if not jugador.ptos_jugadores:
            raise ValueError("No existe registro")
        nombre = validar_nombre(input("Digame el nombre al que quiere buscar su puntaje: "))
        promedio = jugador.average(nombre)
        
        print(f"El average del jugador: {nombre}: {promedio:.2f}")
         
    except ValueError as e:
        print(f"Error ocurred {e}")          

        
if __name__ == "__main__":
    main()