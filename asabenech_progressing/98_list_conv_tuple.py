from typing import List, Tuple

def collection_nim_max(numeros: list)-> Tuple:
    return min(numeros),max(numeros) 

if __name__ == "__main__":
    numeros = [3,4,5,6,7,8,90]
    print(f"La tupla con el menos y le mayor  es: {collection_nim_max(numeros)}")
    print(f"El typo es: {type(collection_nim_max(numeros))}")