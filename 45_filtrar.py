
def notas_promedio(estudiantes_notas):
    for alumno, notas in estudiantes_notas.items():
        suma = sum(notas)
        cantidad = len(notas)
        promedio = suma/cantidad
        estudiantes_notas[alumno] = promedio
        
    return estudiantes_notas

def filter_estudent_aproved(lista_estudiantes):
    lista_aprobados = set()
    for alumno, nota in lista_estudiantes.items():
        if nota >= 3:
            lista_aprobados.add(alumno)
    if not lista_aprobados:
        print("No existen aprobados...")
        return None
    
    return lista_aprobados

def main():
    estudiantes_notas = {"Yoeny": [4,5,3,2,2,2,2], 
                         "Dunieska": [2,2,2,2,2,2,5], 
                         "Nelson": [2,2,2,2,2,2,5]}
    
    student_average = notas_promedio(estudiantes_notas)
    
    aproved_student = filter_estudent_aproved(student_average)
    if aproved_student:
        print(f"Los aprobados son: {aproved_student}")
    
if __name__ == "__main__":
    main()