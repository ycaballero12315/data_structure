from typing import TypedDict, Dict, List, Tuple

class Pedido(TypedDict):
    num_pedido: str
    elementos_d_pedido: List[Tuple[str, float]]
    estado: str

class Restaurant:
    def __init__(self):
        self.check_pedido: Dict[str, Pedido] = {}
        
    def add_pedido(self, cliente: str, 
                   elementos_d_pedido: List[Tuple[str, float]], 
                   estado: str)->None:
        
        num_pedido = f"pedido_{len(self.check_pedido)+1}"
        
        self.check_pedido[cliente] = Pedido(
            num_pedido = num_pedido,
            elementos_d_pedido = elementos_d_pedido,
            estado = estado
        )
    
    def obtener_pedidos(self)-> Dict[str,Pedido]:
        if not self.check_pedido:
            raise ValueError("se necesita tener un registro de pedidos...")
            return
        else:
            return self.check_pedido
    
def mostrar_pedidos(pedidos):
    for cliente, pedido in pedidos.items():
        print(f"El cliente: {cliente}. Tiene \n")
        print(f"el {pedido["num_pedido"]} \n")
        print("_________________Con los elementos___________\n")
        for nombre, cantidad in pedido['elementos_d_pedido']:
            print(f"Producto: {nombre} ->> Cantidad: {cantidad}")
        print(f"El pedido se encuentra: {pedido['estado']}")
            
def main():
    restaurante = Restaurant()
    
    restaurante.add_pedido("yoeny",
                           [("durofrio", 56)],
                           "endiente") 
       
    restaurante.add_pedido("dunieska",
                           [("blumer", 70)],
                           "entregado")
    
    mostrar_pedidos(restaurante.obtener_pedidos())  

if __name__== "__main__":
    main()