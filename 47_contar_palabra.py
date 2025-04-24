from collections import Counter
import string

def contar_palabra():
    frase = input("frase a la que va a analizar: ")
    tabla_de_traduccion = str.maketrans("", "", string.punctuation)
    frase = frase.translate(tabla_de_traduccion)
    frase = frase.lower()
    frase = frase.split()

    conteo = Counter(frase)

    return dict(conteo)


def main():
    conteo_palabras = contar_palabra()

    for palabra, cantidad in conteo_palabras.items():
        print(f"La palabra {palabra} se repite: {cantidad} veces")

if __name__ == "__main__":
    main()

