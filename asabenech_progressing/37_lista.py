from functools import reduce

def insertar():
    lista = []
    while True:
      n = int(input("Numero para insertar (recuerde el 0 para parar): "))
      if n == 0:
          print("Salimos de la ejecucion")
          break
      lista.append(n)
    return lista

def eliminar(n, lista):
    if lista and n in lista:
        indice = lista.index(n)
        del lista[indice]
        print("Elemento eliminado")
    else:
        print("Elemento no encontrado")

def suma(lista):
    sumar = reduce(lambda x, y : x+y, lista)
    return sumar

def menores(n, lista):
    return list(filter(lambda x: x<n, lista))

def contar_apariciones(lista):
    conteo = {}
    for num in lista:
        if num in conteo:
            conteo[num] += 1
        else:
            conteo[num] = 1
    result = [(num, f"aparece: {cant}") for num, cant in conteo.items()]
    return result
    
def main():
    print("Opciones de la lista: ", end="\n")
    print("2. Eliminar elemento ")
    print("3. Sumar elementos de la lista ")
    print("4. Lista de numeros menores al numero dado ")
    print("6. Contar apariciones del numero ")
    

    lista = insertar()
    print(f"La lista es: {lista}")
    option = int(input("Digame su opcion: "))
    match option:
        case 2:
           n = int(input("Elemento a eliminar: "))
           eliminar(n, lista) 
        case 3:
            print(f"la suma de todos los elementos de la lista: {suma(lista)}")
        case 4:
            n = int(input("Digame el numero que quiere comparar: "))
            print(f"la nueva lista es: {menores(n,lista)}")
        case 5:
            print(f"Numeros y sus apariciones: {contar_apariciones(lista)}")
            
   
if __name__ == "__main__":
    main()