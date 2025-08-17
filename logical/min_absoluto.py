def ads_numero(list_numeros):
    try:
        if not all(isinstance(x, (int, float)) for x in list_numeros):
            raise ValueError("Todos los elementos de la lista deben ser números (int o float).")
        if len(list_numeros) == 0:
            raise ValueError("La lista no debe estar vacía.")
        return min(list_numeros, key=lambda x: (abs(x),x))
    except ValueError as e:
        return str(e)

#Salida de ejemplo
print(ads_numero([7, -4, 4, -7]))
 
