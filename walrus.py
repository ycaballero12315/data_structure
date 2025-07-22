elm = [8,9,5,6]
calculo = [y for x in elm if (y:=(lambda x : x**2)(x))>10]

print(calculo)

entradas = []

while (entrada:=input("Escribe una palabra (o 'salir' para terminar): ")) != 'salir'.strip().lower():
    entradas.append(entrada)
    
print(entradas)
    