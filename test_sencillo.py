from functools import reduce

n = int(input('Digame la cant de elem: '))

def test(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum

print(test(n))    
result = reduce(lambda x,y : x+y, range(n))

print(result) 
 