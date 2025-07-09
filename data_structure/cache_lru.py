class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # clave -> nodo
        # Nodos centinela para simplificar inserciones y borrados
        self.head = Node(0, 0)  # dummy head
        self.tail = Node(0, 0)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Quita un nodo de la lista enlazada."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node):
        """Añade un nodo justo después de head (frente)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Mover nodo al frente porque fue usado recientemente
            self._remove(node)
            self._add_to_front(node)
            return node.value
        return -1  # o lanzar excepción si prefieres

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Actualizar valor y mover al frente
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
        else:
            if len(self.cache) == self.capacity:
                # Eliminar el menos usado (nodo antes de tail)
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
            # Insertar nuevo nodo al frente
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))    # devuelve 1, mueve la clave 1 al frente
    cache.put(3, 3)        # elimina clave 2 (menos usada)
    print(cache.get(2))    # devuelve -1 (no encontrada)
    cache.put(4, 4)        # elimina clave 1
    print(cache.get(1))    # devuelve -1
    print(cache.get(3))    # devuelve 3
    print(cache.get(4))    # devuelve 4
