import math

class Fraccion:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero.")
        self.numerador = numerador
        self.denominador = denominador
        self.simplificar()

    def simplificar(self):
        # Simplificar la fracción dividiendo por el MCD
        mcd = math.gcd(self.numerador, self.denominador)
        self.numerador //= mcd
        self.denominador //= mcd

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def __add__(self, otra):
        # Sumar dos fracciones
        numerador = self.numerador * otra.denominador + self.denominador * otra.numerador
        denominador = self.denominador * otra.denominador
        return Fraccion(numerador, denominador)

    def __sub__(self, otra):
        # Restar dos fracciones
        numerador = self.numerador * otra.denominador - self.denominador * otra.numerador
        denominador = self.denominador * otra.denominador
        return Fraccion(numerador, denominador)

    def __mul__(self, otra):
        # Multiplicar dos fracciones
        numerador = self.numerador * otra.numerador
        denominador = self.denominador * otra.denominador
        return Fraccion(numerador, denominador)

    def __truediv__(self, otra):
        # Dividir dos fracciones
        if otra.numerador == 0:
            raise ValueError("No se puede dividir por cero.")
        numerador = self.numerador * otra.denominador
        denominador = self.denominador * otra.numerador
        return Fraccion(numerador, denominador)

    def __eq__(self, otra):
        # Comparar dos fracciones
        return self.numerador == otra.numerador and self.denominador == otra.denominador

# Función para leer fracción
def leer_fraccion():
    numerador = int(input("Ingrese el numerador: "))
    denominador = int(input("Ingrese el denominador: "))
    return Fraccion(numerador, denominador)

# Función principal
def main():
    print("Operaciones con fracciones")

    # Leer dos fracciones
    print("Fracción 1:")
    f1 = leer_fraccion()

    print("Fracción 2:")
    f2 = leer_fraccion()

    print(f"\nFracción 1: {f1}")
    print(f"Fracción 2: {f2}")

    # Sumar
    resultado_suma = f1 + f2
    print(f"\nSuma: {f1} + {f2} = {resultado_suma}")

    # Restar
    resultado_resta = f1 - f2
    print(f"Resta: {f1} - {f2} = {resultado_resta}")

    # Multiplicar
    resultado_multiplicacion = f1 * f2
    print(f"Multiplicación: {f1} * {f2} = {resultado_multiplicacion}")

    # Dividir
    try:
        resultado_division = f1 / f2
        print(f"División: {f1} / {f2} = {resultado_division}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
