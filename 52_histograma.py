from collections import Counter

def histograma(cadena):
    cadena_limpia = [palabra.lower() for palabra in cadena if palabra.isalpha()]

    histo = Counter(cadena_limpia)

    return dict(histo)

def main():
    cadena = input("Digame la cadena de texto:")
    histo = histograma(cadena)
    for k, v in histo.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    main()