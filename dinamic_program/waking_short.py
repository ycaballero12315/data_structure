'''Camino menos costoso'''
def camino_minimo(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    dp = [[0] * columnas for _ in range(filas)]
    
    dp[0][0] = matriz[0][0]

    for i in range(1, filas):
        dp[i][0] = dp[i-1][0] + matriz[i][0]
    for j in range(1, columnas):
        dp[0][j] = dp[0][j-1] + matriz[0][j]

    for i in range(1, filas):
        for j in range(1, columnas):
            dp[i][j] = matriz[i][j] + min(dp[i-1][j], dp[i][j-1])

    return dp[filas-1][columnas-1]


matriz = [
    [1, 3, 101],
    [1, 5, 1],
    [4, 2, 1]
]
print(f'Costo mínimo: {camino_minimo(matriz)}')  # Resultado: 9
