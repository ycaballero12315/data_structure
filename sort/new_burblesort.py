def burble_sort(a): #Algoritmo mas actualizado de busqueda dee burbujas
    size = len(a)
    for i in range(size):
        flag = False
        for j in range(size - 1 - i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                flag = True
        if not flag:
            break
    return a


a = [6, 7, 5, 3]

            
print(burble_sort(a))
            