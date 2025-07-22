from typing import Dict, TypedDict
from datetime import datetime

class Actor(TypedDict):
    nombre:str
    papel:str

class MovieInfo(TypedDict):
    anno_lanzamiento: str
    actores_principales: Dict[str,Actor]

class Pelicula:
    def __init__(self):
        self.peliculas:Dict[str,MovieInfo]={}

    def add_movie(self, titulo: str, anno_lanzamiento: str, 
                 nombre: str, papel: str):

        if titulo in self.peliculas:
            raise ValueError("la pelicula ya se encuentra registrada...")
        else:
            actores = self.peliculas.get(titulo,{}).get("actores_principales", {})
            actor_id = f"actor_{len(self.peliculas) + 1}"
            self.peliculas[titulo] = {
                "anno_lanzamiento": anno_lanzamiento,
                "actores_principales": {
                    **actores,
                    actor_id:{
                        "nombre": nombre,
                        "papel": papel
                    }
                },
            }
    def mostar_registro_peliculas(self)-> list[Dict]:
        if not self.peliculas:
            raise ValueError('registro de peliculas vacio!')
        list_peliculas = []
        for titulo, data in self.peliculas.items():
            peliscula_info = {
                "titulo": titulo,
                "anno_lanzamiento": data["anno_lanzamiento"],
                "actores_principales": [{"nombre_actor": actor["nombre"],
                                         'papel': actor['papel']
                                         } for actor in data["actores_principales"].values()],
            }
            list_peliculas.append(peliscula_info)
                
        return list_peliculas
    
def fecha()-> str:
    try:
        fecha_f = input("Digame la fecha de la pelicula (DD/MM/YYYY): ").strip()

        formato_fecha = datetime.strptime(fecha_f,"%d/%m/%Y")
        formato_string_fecha = formato_fecha.strftime("%d-%m-%Y")
        return formato_string_fecha
    except ValueError:
        print("Fecha insertada incorrectamente")

def main():
    movie = Pelicula()
    while True:
      titulo = input("Nombre de la pelicula: ").strip().lower()
      anno_lanzamiento = fecha()
      nombre_actor = input("Nombre del actor: ").strip().lower()
      papel = input("Papel del actor: ")
      try:
        movie.add_movie(titulo,anno_lanzamiento,nombre_actor,papel)
      except ValueError as e:
        print(f'Error occurred: {e}')
      
      option = input("Digame si desea continuar registrando peliculas (si/no): ").lower()
      if option == 'no':
          break
    
    for elem in movie.mostar_registro_peliculas():
        print(elem)

if __name__ == "__main__":
    main()         
      
      