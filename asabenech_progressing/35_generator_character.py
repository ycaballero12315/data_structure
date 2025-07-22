def generar_n_caracteres(n, character):
    if not isinstance(n, int) or n <= 0:
        print("Numero no valido")
    elif not isinstance(character, str) or len(character) != 1:
        print("Es un solo caracter")
    
    result = character * n
    return result

def main():
    n = int(input("introduzca el numero: "))
    character = input('caracter para concatenar: ')
    print(generar_n_caracteres(n, character))
    
if __name__ == "__main__":
    main()