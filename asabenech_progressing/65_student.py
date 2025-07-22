class Student:
    def __init__(self):
      self.studiante = {}
    
    def student_add(self, nombre: str)->None:
        if nombre not in self.studiante:
          self.studiante[nombre] = {"cursos": {}, "promedio":0.0}

def agregar_curso_calificaciones(obj_student: object, nombre: str, curso: str, 
                                 calificacion: float)-> None:
  
  if nombre not in obj_student.studiante:
    print(f"El alumno {nombre} no se encuentra registrado")
    return
  
  if curso in obj_student.studiante[nombre]["cursos"]:
    print(f"El curso ya curso: {curso} ya se encuentra registrado")
  
  obj_student.studiante[nombre]["cursos"][curso] = calificacion

def calcular_avg_estudiante(obj_student: object, nombre: str)-> None:
  if nombre not in obj_student.studiante and not obj_student.studiante[nombre]["cursos"]:
    print(f"{nombre} no se encuentra en el registro")
    return
  
  notas = obj_student.studiante[nombre]["cursos"].values()
  promedio = sum(notas)/len(notas)
  obj_student.studiante[nombre]["promedio"] = promedio
  
def mostrar_informacion(obj_student: object)-> str:
  if not obj_student.studiante:
    print(f"No existe registro de estudiantes...")
    return
  for nombre, data in obj_student.studiante.items():
    print(f"Estudiante: {nombre}: \n"
          f"Cursos->>>Calificaciones: {data['cursos']} \n"
          f"Promedio: {data['promedio']:.2f}")
    
def main():
  
  stud = Student()
  
  while True:
    nombre = input("Nombre del alumno: ").strip().lower()
    curso = input("Curso: ").strip().lower()
    calificacion = float(input("Calificacion: "))
    stud.student_add(nombre)
    agregar_curso_calificaciones(stud,nombre,curso, calificacion)
    calcular_avg_estudiante(stud, nombre)
    
    continuar = input("¿Desea agregar más estudiantes o cursos? (s/n): ").strip().lower()
    if continuar != "s":
      break
    
  mostrar_informacion(stud)

if __name__ == "__main__":
  main()