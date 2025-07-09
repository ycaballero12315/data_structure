from collections import defaultdict, Counter

cant_duplicados = defaultdict(int)

list_num = [3,4,5,6,3,4,5,6,90,67,4]

for elm in list_num:
    cant_duplicados[elm] += 1

for key, cant in cant_duplicados.items():
    if cant >=2:
        print(f'Elemento {key} duplicado: {cant}')
        
# Alternativa optima
def print_duplicados(list_num):
    
    count = Counter(list_num)
    for item, cant in count.items():
        if cant > 1:
            yield f'Elemento {item}: se repite: {cant}'

# comprobar si la lista tiene duplicados

def comprobar_si_duplicados(list_num):
    return len(list_num) != len(set(list_num))
        

if __name__ == "__main__":
    resultado = print_duplicados(list_num)
    
    for duplicados in resultado:
        print(duplicados)
        
    if comprobar_si_duplicados(list_num):
        print('existen duplicados!!!')