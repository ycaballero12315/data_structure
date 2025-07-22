from typing import List, Dict

def num_max(dict_nums: Dict[int, int])-> Dict[int,int]:
    if not dict_nums:
        return {}
    """Maximo valor dentro de un diccionario"""
    max_id = max(dict_nums, key=dict_nums.get)
    max_num = dict_nums[max_id]
    
    return {
        max_id : max_num 
    }

def del_pares(dict_nums: Dict[int, int])-> Dict[int,int]:
    dict_new = {x: y for x, y in dict_nums.items() if  y%2!=0}
    return dict_new
 
num_dict = {
    4: 34,
    2: 44,
    3: 55,
    1: 77
}

print(num_max(num_dict))
print(f"Elementos impares {del_pares(num_dict)}")

def fusion(dict1, dict2):
    if not dict1 and not dict2:
        return {}
    return dict1 | dict2

num_dict_2 = {
    5:67,
    1:77
}
print(f"Fusion: {fusion(num_dict, num_dict_2)}")

# retornar un diccionario donde los valores de los diccionarios sean iguales
def valores_iguales_diccionario(dict1):
    dict1_values = {}
    for key, value in dict1.items():
        if value not in dict1_values:
            dict1_values[value] = []
        dict1_values[value].append(key)
    return dict1_values

print(f"retorno de funcion: {valores_iguales_diccionario(num_dict)}")