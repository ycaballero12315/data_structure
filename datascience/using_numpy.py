import numpy as np

# print(f"numpy: {np.__version__}")

# print(dir(np))

arr_dimencional = np.array([1,8,9,0])
print(arr_dimencional.shape)
print(arr_dimencional.dtype)
print(arr_dimencional*2)
print(type(arr_dimencional))

numeros = [9,8,5,6,7]

num_float = np.array(numeros, dtype = float)
print(num_float)