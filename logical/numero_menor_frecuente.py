from collections import Counter

def numero_menor_frecuente(A):
    
    if not isinstance(A, list) or not all(isinstance(x, (int, float)) for x in A):
        raise ValueError("La entrada debe ser una lista de números (int o float).")
    if len(A) == 0:
        raise ValueError("La lista no debe estar vacía.")
    
    counter = Counter(A)  
    
    return min(A, key=lambda x: (-counter[x], x))

A = [4, 5, 2, 5, 2, 4, 4, 2]
print(numero_menor_frecuente(A))