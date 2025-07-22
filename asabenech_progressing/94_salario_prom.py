from typing import Dict, List, TypedDict

class Employ(TypedDict):
    name: str
    salary: int

class Empleado_Calc():
    def __init__(self):
        self.list_employ: List[Employ] = []
    
    def add_emp(self, empleado: Employ)->None:
        
        self.list_employ.append(empleado)
    
    def avg_salary(self)-> int:
        suma = 0
        if not self.list_employ:
            return 0
        for employ in self.list_employ:
            suma += employ["salary"]
        return suma/len(self.list_employ)    

if __name__== "__main__":
    empleado1: Employ ={
        'name': "Yoeny",
        'salary': 1000
    }
    empleado2: Employ ={
        'name': "Duni",
        'salary': 2500
    }
    empl_prom_salary = Empleado_Calc()
    empl_prom_salary.add_emp(empleado1)
    empl_prom_salary.add_emp(empleado2)
    print(f"El promedio de salario es: {empl_prom_salary.avg_salary()}")