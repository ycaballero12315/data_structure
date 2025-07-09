from typing import Dict, Any

def fibo(n: int) -> int:
    memo: Dict[Any] = {}
    if n <= 1:
        return 1
    if n not in memo:
        memo[n] = fibo(n-1) + fibo(n-2)
    
    return memo[n]

if __name__ == "__main__":
    n = int(input('Numero a calculat fibonnasi: '))
    print(f"La serie fibonassi es: {fibo(n)}")