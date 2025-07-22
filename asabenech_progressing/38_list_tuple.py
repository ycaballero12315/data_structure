viajeros = [
    ("Manuel Juarez", 19823451, "Liverpool"),
    ("Silvana Paredes", 22709128, "Buenos Aires"),
    ("Rosa Ortiz", 15123978, "Glasgow"),
    ("Luciana Hernandez", 38981374, "Lisboa")
]

ciudades = [
    ("Buenos Aires", "Argentina"),
    ("Glasgow", "Escocia"),
    ("Lisboa", "Portugal"),
    ("Liverpool", "Inglaterra"),
    ("Madrid", "España")
]

def insert_pasajero():
    nombre = input("Ingrese el nombre del pasajero: ")
    dni = int(input("Ingrese el DNI del pasajero: "))
    destino = input("Ingrese el destino del pasajero: ")
    viajeros.append((nombre, dni, destino))
    print(f"El pasajero {nombre} fue agregado con exito ")
    return

def insert_ciudad():
    ciudad = input("Ingrese el nombre de la ciudad: ")
    pais = input("Ingrese el nombre del país: ")
    ciudades.append((ciudad, pais))
    print(f"{ciudad} agregada con exito ")
    return
    
def search_ciudad(dni):
    for p in ciudades:
        if p[1] == dni:
            print(f"El pasajero con DNI {dni} viaja a {p[2]}.")
            return
    print("El DNI no se encuentra!")
    return

def cant_p_ciudad(ciudad):
    cant_p = sum(1 for p in viajeros if p[2] == ciudad)
    print(f"A la ciudad {ciudad}:{cant_p}")
    return

def pasajero_pais(dni):
    for p in viajeros:
        if p[1] == dni:
            for c in ciudades:
                if p[2] == c[0]:
                    pais = c[1]
                    print(f"{p[0]} viaja a {pais}")
                    return
        
    print(f'{dni} no encontrado')

def cant_pasajeros_pais(pais):
    suma_viajero = 0
    for p in ciudades:
        if p[1] == pais:
            ciudad = p[0]
            suma_viajero += sum(1 for v in viajeros if v[2] == ciudad)
    print(f"A {pais} van {suma_viajero} pasajeros")
    return
    
def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Agregar pasajero")
    print("2. Agregar ciudad")
    print("3. Ver ciudad de un pasajero por DNI")
    print("4. Contar pasajeros a una ciudad")
    print("5. Ver país de un pasajero por DNI")
    print("6. Contar pasajeros a un país")
    print("7. Salir")
     
def ejecucion_end():
    print('Fin de la ejecucion!!!') 

def main():
    while True:
        mostrar_menu()
        option = int(input("Opcion que escoge: "))
        
        if option == 1:
            insert_pasajero()
        elif option == 2:
            insert_ciudad()
        elif option == 3:
            dni = int(input("Pasajero a buscar: "))
            search_ciudad(dni)
        elif option == 4:
            ciudad = input("Ciudad a que se desea ver la cantidad de pasajeros: ")
            cant_p_ciudad(ciudad)
        elif option == 5:
            dni = int(input("Pasajero a buscar: "))
            pasajero_pais(dni)
        elif option == 6: 
            pais = input("pais a los que va a cancular la cantidad de pasajeros: ")
            cant_pasajeros_pais(pais)
        elif option == 7:
            ejecucion_end()
            break
        else:
            print('opcion no valida, continuo intentandolo...')

if __name__ == "__main__":
    main()