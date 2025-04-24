def primary_student():
    list_student_p = set()
    while True:
        name = input('Nombre del estudiante de Primaria (o "x" para terminar): ').lower()
        if name == "x":
            break
        list_student_p.add(name)
    return list_student_p

def secundary_student():
    list_student_s = set()
    while True:
        name = input('Nombre del estudiante de Secundaria (o "x" para terminar): ').lower()
        if name == "x":
            break
        list_student_s.add(name)
    return list_student_s

def search_repet_name(list_p, list_s):
    return list_p & list_s

def search_not_repet_name(list_p, list_s):
    return list_s - list_p

def main():
    primary = primary_student()
    secundary = secundary_student()
    
    repet = search_repet_name(primary, secundary)
    no_repet = search_not_repet_name(primary, secundary)
    
    if repet:
        print(f"los nombres repetidos son: {repet}")
    elif no_repet:
        print(f"Los nombres no repetidos son {no_repet}")
    else:
        print("Error inesperado...")
            
if __name__ == "__main__":
    main()
    