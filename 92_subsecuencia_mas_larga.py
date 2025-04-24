from itertools import combinations
"""metodo de fuerza bruta encontar la mayor cadena creciente en una lista"""
def lis_sub_secuencia_mas_larga(arr):
    n = len(arr)
    max_lenth = 0
    lis = []
    for i in range(1, n+1):
        for comb in combinations(arr,i):
            if list(comb) == sorted(comb):
                if len(comb) > max_lenth:
                    max_lenth = len(comb)
                    lis = comb      
    return max_lenth, list(lis)

arr = [4,5,8,9,67, 70, 80, 6,8,9]

max_lenth, lis = lis_sub_secuencia_mas_larga(arr)
print(f"la subsecuencia mas larga es: {lis} y su tamanno es de: {max_lenth}")

"""Programacion dinamica"""

def lis_dp(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return list(dp)

print(lis_dp(arr))