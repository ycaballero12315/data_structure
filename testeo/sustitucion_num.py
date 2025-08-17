from collections import Counter

arr = range(100)
list_num = ['fizzbuzz' if num%5 == 0 and num%3 == 0
            else 'fizz' if num%3 == 0 
            else 'buzz' if num%5 == 0
            else num for num in arr]

print('\n'.join(str(item) for item in list_num))

"""Anagramas"""

def isanagramas(frase:str, otrafrase:str):
    if frase == otrafrase:
        return False
    return sorted(frase.lower()) == sorted(otrafrase.lower())
    
print(f"{isanagramas("amor", 'Roma')}")

def serie_fibo(n):
    if n < 0:
        return 0
    elif n == 1:
        return 1
    else:
        return serie_fibo(n-2) + serie_fibo(n-1)

print(f'Serie fibo de n: {serie_fibo(10)}')
    
def fibo_iterativa(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    a, b = 0, 1
    for _ in range(2,n+1):
        a, b = b, a + b
    return b

print(f'Este es el fibo iterativo:{fibo_iterativa(10)}')

def isprimo() -> list:
    numeros = []
    for num in range(1,101):
        if num >= 2:
            isdivisible = False
            for index in range(2, num):
                if num % index == 0:
                    isdivisible = True
                    break
        else:
            isdivisible = True
        numeros.append(not isdivisible)
    return numeros

def print_isprimo() -> str:
    temp = isprimo()
    for index, i in enumerate(temp, start=1):
        if i == True:
            print(f'{index} Numero primo')
        else:
            print(f'{index} Numero no es primo')
            
print(print_isprimo())

def stringreverse(frase):
    lengt_text = len(frase)
    reverse_text = ''
    for index in range(0, lengt_text):
        reverse_text += frase[lengt_text-index-1]
    return reverse_text

print(stringreverse("Hola mundo"))
    
def operations(value):
    return lambda fist_elm, secund_elm: fist_elm * secund_elm + value

print(operations(3)(5,7))

def agregate_value(value):
    return value + 1

def two_values_and_three_value(first, secund):
    return agregate_value(first + secund)

print(two_values_and_three_value(4,5))

def incrementar_value():
    def pluss(value):
        return value + 10
    return pluss

print(incrementar_value()(20))

# Built-in Higher Order Function
test_arr = [4,6,7,8,9]

aplicate_map = list(map(lambda n, m: n + m, test_arr[:-1], test_arr[1:]))
print(f'La suma de los elementos son: {aplicate_map}')

print("Hola comunidad, creo que ahora si estoy escribiendo sin mirar al teclado, como lo estoy haciendo, lo hago bien o mal")

