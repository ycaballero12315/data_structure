from typing import List, Dict, TypedDict

class Reviwes(TypedDict):
    comment: str
    puntuation: int

class Product(TypedDict):
    name: str
    reviwers: List[Reviwes]

class Mang_Product:
    def __init__(self):
        self.products: List[Product]= []
        
    def add_product(self, name: str)-> str:
        self.products.append({'name':name, "reviwers": []})
        return f"Producto agregado con exito!"
    
    def add_product_review(self, name:str, comment: str, puntuation: int)->str:
        if len(self.products) == 0:
            return 'No existen productos en la lista!'
        for product in self.products:
            if product["name"] == name:
                if 1<=puntuation<=5:
                    product['reviwers'].append({'comment':comment, 'puntuation': puntuation})
                    return 'Insertada la revision con exito!'
                return f'la puntuacion debe estar entre {1} y {5}'
            
    def show_product(self)->str:
        if not self.products:
            return 'No existen productos en la lista!'
        else: 
            result = []
            for product in self.products:
                element = [f"Nombre: {product['name']}"]
                if not product['reviwers']:
                    element.append('No existen revisiones')
                else:
                    for idx, reviwers in enumerate(product['reviwers'], start=1):
                        element.append(f'La revision {idx},comentario: {reviwers['comment']}, puntuacion: {reviwers['puntuation']}')
                result.append('\n'.join(element))
                
        return '\n\n'.join(result)  
         
if __name__ == "__main__":
    manager_prod = Mang_Product()
    manager_prod.add_product("Monitor")
    manager_prod.add_product_review("Monitor", 'este es un comentario', 5)
    print(manager_prod.show_product())
    
                            
                    
             