from typing import Dict

class Store:
    def __init__(self):
        self.inv_producto = {}
        
    def add_product(self, producto: str)->None:
        if producto not in self.inv_producto:
            self.inv_producto[producto] = {"precio":0.0, "cant": int}
    
    def print_inventario(self, producto: str)-> Dict[str,Dict[float, int]] :
        if not self.inv_producto:
            raise ValueError("No existe registro de inventario")
        return {
            producto:{
                "precio": data['precio'],
                "cantidad": data["cant"]
            }
                for producto, data in self.inv_producto.items()
        }

def add_precio_cant(obj_store, producto: str, precio: float, cantidad: int)->None:
    if producto not in obj_store.inv_producto:
        print(f"{producto} no se encuentra en el store")
        return
    
    obj_store.inv_producto[producto]["precio"] = precio
    obj_store.inv_producto[producto]["cant"] = cantidad

def mostrar_inv(obj_store, producto)->str:
    registro = obj_store.print_inventario(producto)
    if not registro:
        print(f"No existe registro del producto: {producto}")
    for nombre, data in registro.items():
        print(f"Nombre: {nombre}\n"
              f"Precio: {data['precio']}\n"
              f"Cantidad: {data['cantidad']}")

def main():
    obj_store = Store()
    while True:
        producto = input("Digame el producto: ").strip().lower()
        obj_store.add_product(producto)
        
        if producto not in obj_store.inv_producto:
            raise ValueError(f"No se encuentra el {producto} en el inventario")
        
        precio = float(input(f"Precio del producto ({producto}): "))
        if precio <= 0:
            raise ValueError("El pecio del producto tiene que ser mayor a cero ")
        
        cantidad = int(input("Cantidad de productos: "))
        
        add_precio_cant(obj_store, producto, precio, cantidad)
        
        option = input(f"Desea continuar inventariando productos? (si/no): ").strip().lower()
        if option == "no":
            break
        
    mostrar_inv(obj_store,producto) 
    
if __name__ == "__main__":
    main()        
    