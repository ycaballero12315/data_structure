from typing import List, Any

def mochila(elems: List[int],W:int, values_m: List[int])->Any:
    n = len(elems)
    
    dp = [[0]* (n+1) for _ in range(W+1)]
    
    for i in range(1, n + 1): # pesos de los items
        for w in range(1, W + 1):
            if elems[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], values_m[i-1] + dp[i-1][w-elems[i-1]])
            else:
                dp[i][w] = dp[i-1][w]
    return[n][W]

if __name__ == "__main__":
    elems = [4,6,8,12]
    values = [150, 200, 560,100]
    W = 13
    print(f'la mochila lograra tener un valor de {mochila(elems, W, values)}')

