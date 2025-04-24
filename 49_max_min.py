def crear_dict(lista):
    elem_unicos = set()
    dict_elem = {}

    for idx, valor in enumerate(lista):
        if valor not in elem_unicos:
            elem_unicos.add(valor)
            dict_elem[idx] = int(valor)
    
    return dict_elem

def lista_values(dictionary):
    
    return list(dictionary.values())

def max_value(list_value):
    return max(list_value)


def min_value(list_value):
    return min(list_value)

def main():
    entrada = input("Listado de elementos para formar el diccionario (recuerde son numeros): ")
    lista = entrada.split(",")
    diccionario = crear_dict(lista)
    valores = lista_values(diccionario)
    print(f"El maximo en {valores} es: {max_value(valores)}")
    print(f"El minimo en {valores} es: {min_value(valores)}")

if __name__ == "__main__":
    main()