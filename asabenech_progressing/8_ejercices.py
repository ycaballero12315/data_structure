def divisible():
    num_div = list(filter(lambda x: x%2 == 0 and x%5 == 0, range(1,101)))
    return num_div

print(f'Los numeros divisibles por 2 y 5 del 1-100: {divisible()}')