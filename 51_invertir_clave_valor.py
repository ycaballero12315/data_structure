def invertir_diccionario(dictionary):
    dict_new = {value: key for key, value in dictionary.items()}
    return dict_new

dictionary = {
    "a": 12,
    "b": 17
}

print(invertir_diccionario(dictionary))