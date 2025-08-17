def ads_numero(list_numeros, T):
    try:
        if not all(isinstance(x, (int, float)) for x in list_numeros):
            raise ValueError("Todos los elementos de la lista deben ser números (int o float).")
        if len(list_numeros) == 0:
            raise ValueError("La lista no debe estar vacía.")
    
        return min(list_numeros, key=lambda x: (abs(sum(int(d) for d in str(abs(int(x)))) - T), x))
        
    
    except ValueError as e:
        return str(e)

lista_num = [91, 82, 73, 64, 55, -70]
print(ads_numero(lista_num, 9))