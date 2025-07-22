def knapsack(pesos, valores, capacidad):
    n = len(valores)
    matriz = [[0 for _ in range(capacidad + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacidad + 1):
            if pesos[i - 1] <= w:
                incluir = valores[i - 1] + matriz[i - 1][w - pesos[i - 1]]
                no_incluir = matriz[i - 1][w]
                matriz[i][w] = max(incluir, no_incluir)
            else:
                matriz[i][w] = matriz[i - 1][w]

    return matriz[n][capacidad]

pesos = [2, 3, 4, 5]
valores = [3, 4, 5, 6]
capacidad = 5

resultado = knapsack(pesos, valores, capacidad)
print(f'Valor máximo que cabe en la mochila: {resultado}')
