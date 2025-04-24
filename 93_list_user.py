from typing import List, Dict, TypedDict

class Producto(TypedDict):
    id: int
    nombre_prod: str
    detalles: str
class Pedido(TypedDict):
    list_productos:List[Producto]

class Usuario(TypedDict):
    nombre: str
    correo: str
    list_pedidos: List[Pedido]

class Gestionar_User:
    def __init__(self)-> None:
        self.list_user: List[Usuario]= []
        
    def add_user(self, nombre: str, correo: str, list_pedidos: List[Pedido])->None:
        new_user: Usuario = {
            "nombre": nombre,
            "correo": correo,
            "list_pedidos": list_pedidos
        }
        self.list_user.append(new_user)
    
    def show_user(self)->str:
        
        if not self.list_user:
            return "El registro no existe."
        result = []
        for idx, user in enumerate(self.list_user, start=1):
            user_info = [f"Usuario: {idx}"]
            user_info.append(f"nombre: {user['nombre']}")
            user_info.append(f"e_mail: {user['correo']}")
            user_info.append("\n Lista de Pedidos:")
            if user['list_pedidos']:
                for user_idx, pedido in enumerate(user['list_pedidos'], start=1):
                    user_info.append(f"Pedido: {user_idx}")
                    for producto in pedido:
                        user_info.append(f'Producto: {producto['id']}')
                        user_info.append(f"Nombre producto: {producto['nombre_prod']}")
                        user_info.append(f'Detalles del producto: {producto['detalles']}')
            else:
                user_info.append("\n No existen pedidos...")
            result.append(f'\n'.join(user_info))
        return '\n\n'.join(result)


if __name__ == "__main__":
    gestionar = Gestionar_User()
    
    # Crear pedidos
    producto1: Producto = {"id": 1, "nombre_prod": "Laptop", "detalles": "Dell XPS 13"}
    producto2: Producto = {"id": 2, "nombre_prod": "Mouse", "detalles": "Logitech MX Master 3"}
    pedido1: Pedido = [producto1,producto2]

    
    # Agregar usuarios
    gestionar.add_user("Juan Pérez", "juan.perez@example.com", [pedido1])
    gestionar.add_user("Ana Gómez", "ana.gomez@example.com", [])
    
    # Mostrar usuarios
    usuarios_info = gestionar.show_user()
    print(usuarios_info)
            
    