import numpy as np
import gc

arr = np.zeros((10000, 10000))  # ~800 MB
print(arr)

del arr
gc.collect()

lista = [7, 8, 9]

vacia = "Vacia" if not lista else "Llena"

print(vacia)


def par_impart(n):
    return 'Par' if n % 2 == 0 else 'Impar'


print(par_impart(10))

