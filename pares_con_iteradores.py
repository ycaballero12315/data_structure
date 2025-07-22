class NumerosPares:
    def __init__(self, begin):
        self.begin = begin
        
    def __iter__(self):
      self.x = 2
      return self
    def __next__(self):
        if self.x > self.begin:
            raise StopIteration
        continuar = self.x
        self.x += 2
        return continuar
    

pares = NumerosPares(10)
for num in pares:
    print(num)


def pares_lim(lim):
    num = 2
    while num <= lim:
        yield num
        num += 2

pares = pares_lim(100)
for num in pares:
    print(num)
 
def impares(lim):
    n = 1
    while n <= lim:
        if n % 2 !=0:
            yield n
        n += 1

impar = impares(10)

for i in impar:
    print(i)