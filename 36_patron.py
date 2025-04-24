def phater(lista, patron):
    for i in lista:
        print(f"{i*patron}")

def main():
    
    lista = [3, 5, 8]
    phater(lista, "*")

if __name__ == "__main__":
    main()