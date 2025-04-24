def mcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
      a, b = b, a % b
    return a

if __name__ == "__main__":
    a = int(input("Primer numero: "))
    b = int(input("Segundo numero: "))
    
    print(f"El minimo comun divisor entre {a} y {b} es: {mcd(a,b)}")
    
