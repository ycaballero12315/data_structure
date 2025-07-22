from typing import List

class Producto_Q:
    def __init__(self, nombre: str, 
                 gramaje: float):
        self.nombre = nombre
        self.gramaje = gramaje
        
class Medicamento:
    def __init__(self, nombre: str, 
                 codigo: int, f_vencimiento: str):
        self.productos_q: List[Producto_Q] = []
        self.nombre = nombre
        self.codigo = codigo
        self.f_vencimiento = f_vencimiento
    
    def add_productos_quimicos(self, q: Producto_Q):
        if len(self.productos_q) < 10:
            self.productos_q.append(q)
    
    def product_q_mas_utilizado(self)-> str:
        return max(self.productos_q, key=lambda q : q.gramaje).nombre
    
    def productos_q_x_medicamentos(self)-> List[Producto_Q]:
        return sorted(self.productos_q, key=lambda q : q.gramaje, reverse=True)
    
    def search_medicamento_x_gramaje(self, name_pro_q: str) -> str:
        for q in self.productos_q:
            if q.nombre == name_pro_q:
                return f'El producto es: {q.nombre} el gramaje utilizado es: {q.gramaje}'
            
        return f'Nombre del quimico no aparece!'
    
    def etiqueta_venta(self, name_pro_q: str):
        medicamentos = self.search_medicamento_x_gramaje(name_pro_q)
        return '\n'.join(f'{q.nombre}: {q.gramaje}g' for q in medicamentos)

class ControlMed:
    def __init__(self):
        self.medicamentos: List[Medicamento] = []
    
    def add_medicamento(self, m: Medicamento):
        self.medicamentos.append(m)
        
    def obener_medicamento(self, nombre_medicamento: str) -> Medicamento:
        for m in self.medicamentos:
            if m.nombre == nombre_medicamento:
                return m
        return None
    
    def listar_medicamentos(self):
        return [m.nombre for m in self.medicamentos]        
    
    def print_medicamentos(self):
        for m in self.medicamentos:
            print(f'Medicamento: {m.nombre} -> Codigo: {m.codigo}')
            print('ingredientes: ')
            for i in m.productos_q_x_medicamentos():
                print(f'Nombre: {i.nombre} : {i.gramaje}')
                        
if __name__ == "__main__":
    pq = Producto_Q('metafetamina', 100)
    pq1 = Producto_Q('otros', 137.9)
    m = Medicamento('bicarbonato', 34, '25 de febrero del 2026')
    m1 = Medicamento('nobatropin', 45, '30 de febrero del 2026')
    c = ControlMed()
    c.add_medicamento(m)
    c.add_medicamento(m1)
    print(f"el medicamento es el: {(c.obener_medicamento('nobatropin')).codigo}")
    
    