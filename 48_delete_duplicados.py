def delete_duplicados(lista):
    elem_unicos = set()
    almacen = {}
    for idx, value in enumerate(lista):
        if value not in elem_unicos:
            elem_unicos.add(value)
            almacen[idx] = value
    return almacen


def main():
    entrada = input("Elementos que va a insertar (Recuende que es una lista): ")

    lista = entrada.split(",")

    for idx, valor in delete_duplicados(lista).items():
        print(f"Los elemntos son {idx}:{valor}")

if __name__== "__main__":
    main()