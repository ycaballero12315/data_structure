from typing import Dict, List, Tuple, TypedDict

class Pelicula(TypedDict):
    titulo: str
    actores: List[str]
    detalles: Tuple[str, int]

class Films_Store():
    def __init__(self):
        self.list_peliculas: List[Pelicula] = []
    
    def add_pelicula(self, pelicula: Pelicula):
        self.list_peliculas.append(pelicula)
        
    def show_moviel(self)->str:
        if not self.list_peliculas:
            return "No existe registro de peliculas..."
        result = []
        for idx, pelicula in enumerate(self.list_peliculas, start=1):
            movie_details = [f"Pelicula: {idx}"]
            movie_details.append(f"Titulo: {pelicula['titulo']}")
            movie_details.append("Los actores son: ")
            for actor_idx, actor in enumerate(pelicula['actores'], start=1):
                movie_details.append(f"{actor_idx}.{actor}")
            fecha_creacion, costo = pelicula['detalles']
            movie_details.append(f'La fecha de creacion es: {fecha_creacion}')
            movie_details.append(f"Con un valor de: {costo}")
            result.append("\n".join(movie_details))
        return '\n\n'.join(result)
            
                
if __name__ == "__main__":
    pelicula1: Pelicula = {
        'titulo': "Acccion 4",
        'actores': ['Yoeny', "Dinieska"],
        'detalles': ('23/4/96', 5000)
    }
    films = Films_Store()
    films.add_pelicula(pelicula1)
    print(f"Peliculas: {films.show_moviel()}")    