from typing import TypedDict, List, Tuple

class Temp_City(TypedDict):
    name: str
    temperatures: List[Tuple[str, float]]

class Adm_City:
    def __init__(self):
        self.cities: List[Temp_City] = []
    
    def add_elem(self, name: str, temperatures: List[Tuple[str, float]])->None:
        self.cities.append({"name": name, "temperatures": temperatures})
    
    def show_city(self)-> List[str]:
        if not self.cities:
            return f"No existen las ciudades"
        temp_cities = []
        for idx, city in enumerate(self.cities, start=1):
            temp_cities.append(f'{idx}: Ciudad: {city['name']}: -Temperaturas:{city['temperatures']}')
        return temp_cities 

if __name__ == '__main__':
    city = Adm_City()
    temperatures = [(('23/10/01'), (45.7)), (('25/10/01'), (48.7))]
    city.add_elem('california', temperatures)
    print(city.show_city())         