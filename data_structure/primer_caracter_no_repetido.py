from collections import Counter

def first_character_non_repet(list_num):
    count = Counter(list_num)
    
    for key, value in count.items():
        if value < 2 and value > 0:
            return f'El elemento {key} es el primero que no se repite'

# Metodo mas eficiente porque count no coloca los elementos organizados
def primer_elem_no_rept(seq):
    contar = Counter(seq)
    for elm in seq:
        if contar[elm] == 1:
            return f'El elemento {elm} es el primero que no se repite'
    return "Todos se repiten"

if __name__ == "__main__":
    list_num = [4,5,6,7,8,9,4,5,6,7,8]
    if first_character_non_repet(list_num) is not None:
        print(first_character_non_repet(list_num))
    else:
        print('Elementos todos se repiten')
    
    print(primer_elem_no_rept(list_num))
        