def sumar(lista):
    suma = 0
    for i in lista:
        suma += i 
    return suma

def multip(lista):
    mult = 1
    for i in lista:
        mult *= i
    return mult

def main():
    lista = [34,56,77,78]
    print(f"La suma: {sumar(lista)}, la multiplicacion es: {multip(lista)}")

if __name__ == "__main__":
    main()
    