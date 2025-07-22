from typing import List

class Producto:
    def __init__(self, nombre: str, 
                 cant_existencia: int, vendidas_cant: int,
                 precio_x_unidad: float):
        self.nombre = nombre
        self.cant_existencia = cant_existencia
        self.vendidas_cant = vendidas_cant
        self.precio_x_unidad = precio_x_unidad

class Tienda:
    def __init__(self):
        self.lista_product: List[Producto] = []
        
    def add_producto(self, p: Producto):
        self.lista_product.append(p)
    
    def prod_mas_vendido(self) -> str:
        return max(self.lista_product, key=lambda p : p.vendidas_cant).nombre
    
    def importe_total(self)->float:
        total = sum([(p.vendidas_cant * p.precio_x_unidad) for p in  self.lista_product if p.vendidas_cant > 0])
        return total 
    
    def avg_prod_existencia(self)->float:
        cantidad = [p.cant_existencia for p in self.lista_product if p.cant_existencia > 0]
        promedio = sum(cantidad) / len(cantidad)
        return promedio

    def menor_recaudacion(self) -> str:
        productos_con_ventas = [p for p in self.lista_product if p.vendidas_cant > 0]
        if not productos_con_ventas:
            return 'No se realizaron ventas'
        return min(productos_con_ventas, key=lambda p : p.vendidas_cant * p.precio_x_unidad).nombre
    

if __name__ == "__main__":
    p1 = Producto('cepillo', 49, 50, 170.9)
    p2 = Producto('alambre', 32, 100, 10.50)
    t = Tienda()
    t.add_producto(p1)
    t.add_producto(p2)
    
    print(f'El prod mas vendido es: {t.prod_mas_vendido()}')
    print(f'La ganancia total es: {t.importe_total()}')
    print(f'Queda un promedio en existencia de: {t.avg_prod_existencia()}')
    print(f'Producto de menor recaudacion: {t.menor_recaudacion()}')
    
    