def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def generador_primos():
    n = 2
    while True:
        if es_primo(n):
            yield n
        n += 1

# Obtener los primeros 10 primos
gen = generador_primos()
for _ in range(10):
    print(next(gen))
