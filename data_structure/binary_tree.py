class Node:
    
    def __init__(self, valor):
        self.valor = valor
        self.right = None
        self.left = None
    
def insertar(self, raiz, valor):
    if raiz is None:
        return Node(valor)
    elif valor < raiz.valor:
        raiz.left = insertar(raiz.left, valor)
    else:
        raiz.right = insertar(raiz.right, valor)
    return raiz
    
    