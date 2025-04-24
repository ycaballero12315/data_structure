import math


def area_circ(radio):
    return math.pi * radio**2

def perimetro_circ(radio):
    return 2 * math.pi * radio

if __name__ == "__main__":
    radio = float(input("Digame el radio: "))
    print('Seleccione una opcion: ')
    print("1. Area del Circulo: ")
    print("2. Perimetro del Circulo: ")
    opt = int(input())
    if opt == 1:
        print(f"El area del circulo es: {area_circ(radio)}")
    elif opt == 2:
        print(f"El perimetro del circulo es: {perimetro_circ(radio)}")
    else:
        print("Opcion no valida")



    