def concatenar_dict(dict1, dict2):
    return dict1 | dict2

dict1 = {"Yoe": ["Talla", "Peso"]}
dict2 = {"Yoe": [4,5,3,2,4]}

print(concatenar_dict(dict1, dict2))