def max_min(lista):
    return {
        'maximo': max(lista),
        "minimo": min(lista)
    }

if __name__ == "__main__":
    list_num = []
    cant_num = int(input('Cantidad de numeros: '))
    for _ in range(cant_num):
        num = int(input("Digame el numero: "))
        list_num.append(num)
    for k, v in max_min(list_num).items():
        print(f"{k} : {v}")