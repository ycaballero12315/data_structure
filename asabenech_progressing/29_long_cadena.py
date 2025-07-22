def long_string(cadena):
    contar = 0
    for _ in cadena:
        contar  += 1
    return contar

def main():
    cadena = input("Cadena a ser insertada: ")
    print(f"La cadena {cadena} tiene: {long_string(cadena)} caracteres")

if __name__ == "__main__":
    main()