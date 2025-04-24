def tabla_mult():
    for i in range(2,10):
        print(f'La tabla de multiplicar de {i}')
        for j in range(1, 10):
            print(f"La multiplicacion entre: {i} * {j} = {i*j}")
        print("_________________________________________________")

tabla_mult()