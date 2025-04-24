from typing import List, Any

def max_path_sum(data):
    if not data or not data[0]:
        return 0
    
    m = len(data)
    n = len(data[0])
    
   
    dp = [[0] * n for _ in range(m)]
    print(f'Inicio de la matriz: {dp}')
    dp[0][0] = data[0][0]
    print(f"Guardo el primer elemento en la nueva matriz")
   
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + data[0][j]

    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + data[i][0]
    

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = data[i][j] + max(dp[i-1][j], dp[i][j-1])
    print(dp) 
    
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            print(f"Valores (i->{i}: j->{j}): {dp[i][j]}")
            
    return dp[-1][-1]

data = [
    [5, 4, 5, 4],
    [3, 1, 2, 2],
    [1, 3, 1, 3],
    [3, 2, 2, 1]
]

if __name__ == '__main__':
    sum_max = max_path_sum(data)
    print("Suma máxima:", sum_max)
