from typing import List, Tuple


def ordenar_a_partir_del_segundo(list_tuple)->List[Tuple[int, int]]:
    """Ordenar por la lista de tuplas a partir del segundo elemento"""
    return sorted(list_tuple, key=lambda arguments : arguments[1], reverse=True)

list_tuple = [(2,56), (1,79), (5,45)]

print(f"la tupla organizada es: {ordenar_a_partir_del_segundo(list_tuple)}")

def encontar_mayor_valor_en_tupla(list_tuple)-> Tuple[int, int]:
    """Retorna la mayor tupla dentro de la lista"""
    return max(list_tuple, key=lambda arguments : sum(arguments))

print("la tupla que tiene la mayor suma de sus valores es: "
      f"{encontar_mayor_valor_en_tupla(list_tuple)}")