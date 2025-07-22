from collections import OrderedDict

class LRUCache:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cache = OrderedDict()

    def get(self, clave):
        if clave not in self.cache:
            return -1
        self.cache.move_to_end(clave)  # Marca como "recién usado"
        return self.cache[clave]

    def put(self, clave, valor):
        if clave in self.cache:
            self.cache.move_to_end(clave)
        self.cache[clave] = valor
        if len(self.cache) > self.capacidad:
            self.cache.popitem(last=False)  # Elimina el menos usado


# Uso
cache = LRUCache(2)
cache.put(1, 'A')
cache.put(2, 'B')
print(cache.get(1))  # Devuelve 'A'
cache.put(3, 'C')    # Saca el 2 porque fue el menos usado
print(cache.get(2))  # Devuelve -1 (ya no está)
