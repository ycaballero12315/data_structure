from typing import Dict, List, TypedDict

class Ingredientes(TypedDict):
    nombre: str
    catidad: float
    
class Receta(TypedDict):
    ingredientes: List[Ingredientes]
    instrucciones: List[str]   
     
class Dtalles_Receta(TypedDict):
    nombre: str
    ingredientes: List[Ingredientes]
    instrucciones: List[str]
    
class Recetas:
    def __init__(self):
      self.recetas_cock:Dict[Dtalles_Receta] = {}
    
    def add_receta(self, nombre: str, ingredientes: List[Ingredientes], instrucciones: List[str])->None:
       if nombre in self.recetas_cock:
           raise ValueError(f"La {nombre} ya se encuentra regisrada")
       if not ingredientes or not instrucciones:
           raise ValueError(f"La receta debe tener ingredientes e instrucciones.")
       self.recetas_cock[nombre] = Receta(
           ingredientes = ingredientes,
           instrucciones = instrucciones
       )
    def show_receta(self)-> List[Dtalles_Receta]:
        if not self.recetas_cock:
            raise ValueError('El recetario esta vacio')
        else:
            recetas_detalles:List[Dtalles_Receta] = []
            for nombre, receta in self.recetas_cock.items():
                recetas_detalles.append(
                    Dtalles_Receta(
                        nombre = nombre,
                        ingredientes = receta["ingredientes"],
                        instrucciones = receta["instrucciones"],
                    )
                )
            return recetas_detalles

def main():
    receta = Recetas()
    while True:
        nombre_receta = input("Nombre de la receta: ").strip().lower()
        if not nombre_receta:
            print("Debe insertar un nombre de receta. ")
            break
        ingredientes = [{"huevo": 45},
                        {"harina de trigo": 67}]
        
        instrucciones = ["se hace asi", "se hace asado"]
        
        receta.add_receta(nombre_receta, ingredientes, instrucciones)
        
        option = input("Continuara agregando recetas (si/no): ").lower().strip()
        if option == "no":
            print("Saliendo del programa...")
            break
        
    for elemtos in receta.show_receta():
        print(elemtos)
    
if __name__ == "__main__":
    main()