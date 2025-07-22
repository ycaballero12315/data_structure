"""Ordenamiento x seleccion n**2"""

def select_sort(elem):
    n = len(elem)
    for i in range(n):
        index = i
        for j in range(i+1, n):
            if elem[index]> elem[j]:
                elem[index], elem[j] = elem[j], elem[index]
    return elem

elem = [4,5,6,8,7]

print(select_sort(elem))            
         