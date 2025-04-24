from typing import List, Tuple, Dict, TypedDict

class Student(TypedDict):
    name: str
    degree: Tuple[float, ...]
    
class Students:
    def __init__(self):
        self.students: List[Student] = [
        {"name": "Ana", "califications": (90, 85, 88)},
        {"name": "Luis", "califications": (75, 80, 78)},
        {"name": "Carlos", "califications": (92, 95, 91)},
        {"name": "Sofia", "califications": (85, 88, 86)},]
    
    def students_orderby_max_calification(self)-> List[Student]:
        return sorted(self.students, key=lambda e: (sum(e['califications'])/len(e['califications'])), reverse=True)
    

if __name__ == "__main__":
    stud = Students()
    print(f'la lista de estudiantes es: {stud.students_orderby_max_calification()}')
    for student in stud.students:
        avg = sum(student['califications'])/len(student['califications'])
        print(f'Alumno: {student['name']} - Promedio: {avg:.2f}')
    
    
        