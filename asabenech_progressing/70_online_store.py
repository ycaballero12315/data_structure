from typing import TypedDict, Dict, List
import re

class Producto(TypedDict):
    nombre_p: str
    catidad: int

class Compra(TypedDict):
    id_compra: int
    producto : Producto

class Tienda:
    
    def __init__(self):
        self.sheaps_user: Dict[str, Compra] = {}
        self.id_compra: int = 1
        
    def add_compra(self, nombre_cliente, nombre_p: str, cantidad: int)->None:
        
        self.sheaps_user[nombre_cliente] = Compra(
            id_compra = self.id_compra,
            producto = Producto(
                nombre_p = nombre_p,
                catidad = cantidad
            ),
        )
        self.id_compra += 1
    
    def mostrar_compra(self)->Dict[str,Compra]:
        if not self.sheaps_user:
            raise ValueError("No existen elementos en el registro")
        
        compra_d_cliente: List[Dict[str, Compra]] = []
        identificador = f'compra_{len(compra_d_cliente)+1}'
        for nombre_cliente, shoping in self.sheaps_user.items():
                compra_d_cliente.append(
                    {"identificador": identificador,
                    "nombre_cliente": nombre_cliente,
                    "compra": Compra(
                        id_compra = shoping["id_compra"],
                        producto = shoping["producto"]
                    )
                },)
                
        return compra_d_cliente

def main():
    store = Tienda()
    patron = r'^[A-Za-záéíóúÁÉÍÓÚÑñ\s]+$'
    
    while True:
        nombre_cliente = input("Nombre del cliente: ").strip().lower()
        if not nombre_cliente and not re.match(patron, nombre_cliente):
            print("Debe insertar un nombre valido de cliente: ")
            break
        nombre_producto = input("Nombre del producto: ").strip().lower()
        cantidad = int(input(f"cantidad de {nombre_producto}: "))
        if cantidad <= 0:
            print("La cantidad tiene que ser mayor que cero.")
            break
        
        try:
          store.add_compra(nombre_cliente,nombre_producto,cantidad)
        except ValueError as e:
          print(f'Error occurred {e}')
        
        option = input("Desea continuar insertando valores (si/no)").strip().lower()
        if option != "si":
            print("Saliendo del programa...")
            break
        
    print(f"El resultado es: {store.mostrar_compra()}")

if __name__ == "__main__":
    main()