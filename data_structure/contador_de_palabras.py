from collections import Counter
import string

def contar_palabras(frase):
    tabla = str.maketrans('','', string.punctuation)
    texto_limpio = frase.translate(tabla).lower()
    palabras = texto_limpio.split()
    count = Counter(palabras)
    for key, cantidad in count.items():
        yield f'{key} se repite: {cantidad}'


if __name__ == "__main__":
    frase = "Hola yo soy Hola, la palabra repetida"
    repet_palabras = contar_palabras(frase) 
    for item in repet_palabras:
        print(item)   
    
    
    