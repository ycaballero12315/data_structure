from typing import List, Tuple

def pares_e_impares(lista)-> List[Tuple[int, None]]:
    pares = [(num, ) for num in lista if num%2==0]
    impares = [(num, )for num in lista if num%2 !=0]
    return pares, impares

lista = [3, 5, 6, 8,90]

print(pares_e_impares(lista))