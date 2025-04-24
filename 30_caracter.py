def caracter_vocal(vocal):
    list_vocal = ["a", "e", "i", "o", "u"]
    if vocal in list_vocal:
        resul = True
    else:
        resul = False
    return resul
        
def main():
    vocal = input("Digame el caracter: ")
    print(f"El resultado es: {caracter_vocal(vocal)}")

if __name__ == "__main__":
    main()