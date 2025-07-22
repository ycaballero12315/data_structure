def delete_key(diccionario, umbral):
    return {key: valor for key, valor in diccionario.items() if valor <= umbral}

def main():
    diccionario = {
        "a": 1,
        "b": 5,
        "c": 6,
        "d": 7,
        "e": 10
    }
    umbral = int(input("Digame el umbral: "))
    diccionario_filtro = delete_key(diccionario, umbral)

    for key, valor in diccionario_filtro.items():
        print(f"{key}: {valor}")

if __name__== "__main__":
    main()