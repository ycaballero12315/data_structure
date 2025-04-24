def create_dict_a_list(contactos, numeros):

    if len(numeros) != len(contactos):
        raise ValueError("Los conjuntos deben ser del mismpo tamanno!!!")
    
    new_dictionary = {contactos:numeros for contactos, numeros in zip(contactos,numeros)}
    return new_dictionary

def main():
    contactos = ("Yoeny", "Dunienka", "Samuel")
    numeros = (234, 234, 567)
    dictionary = create_dict_a_list(contactos, numeros)
    for k, v in dictionary.items():
        print(f"{k}: {v}")

if __name__== "__main__":
    main()