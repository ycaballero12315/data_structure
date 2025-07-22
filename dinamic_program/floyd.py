class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def has_cycle(head):
    if not head or not head.next:
        return False
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def detectar_inicio_ciclo(head):
    tortuga = head
    liebre = head

    # Paso 1: Detectar si hay ciclo
    while liebre and liebre.next:
        tortuga = tortuga.next
        liebre = liebre.next.next
        if tortuga == liebre:
            break
    else:
        return None  # No hay ciclo

    # Paso 2: Encontrar el inicio del ciclo
    tortuga = head
    while tortuga != liebre:
        tortuga = tortuga.next
        liebre = liebre.next

    return tortuga  # Nodo donde inicia el ciclo
   
        
        
        
# Ejecuciones
# Crear una lista enlazada simple
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d
d.next = b  # ← Esto crea un ciclo

print(has_cycle(a))  # Imprime True


# Crear una lista enlazada con ciclo
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d
d.next = b  # Ciclo empieza en 'b'

inicio = detectar_inicio_ciclo(a)
if inicio:
    print(f'El ciclo comienza en el nodo con valor: {inicio.value}')
else:
    print('No hay ciclo en la lista.')
