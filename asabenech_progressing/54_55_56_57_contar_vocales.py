import re

def contar_vocales(frase):
    vocales = ["a","o","u","i","e"]
    frase = re.sub(r'[^a-zA-Z]','',frase.lower())
    
    contador = {vocal: 0 for vocal in vocales}
    
    for caracter in frase:
        if caracter in contador:
            contador[caracter] += 1
    return contador

#ordenar un diccionario por el valor
def dictionary_elem_order(dictionary):
    ordened_dictionary = dict(sorted(dictionary.items(),key=lambda item : item[1]))
    return ordened_dictionary

def optimo_dictionary_elem_order(dictionary):
    ordened_dictionary = {k:v for k, v in sorted(dictionary.items(), key=lambda item: item[1])}
    return ordened_dictionary

#Comprobar si el diccionario esta vacio
def es_diccionario_vacio(dictionary):
    return len(dictionary) == 0

#dada una clave del diccionario buscarla y devolver su valor
def key_search(key, dictionary):
    return dictionary.get(key)

def delete_elemnt_dict(key, dictionary):
    
    element = dictionary.pop(key, None)
    
    
       
def opciones():
    print("1. contar Vocales (Devuelve un diccionario con las vocales y su cantidad de apariciones)")
    print("2. Oredenar el diccionario de vocales por la cantidad (metodo tradicional): ")
    print("3. Oredenar el diccionario de vocales por la cantidad (metodo optimizado): ")
    print("4. Diccionario vacio ")
    print("5. Encontrar un valor dada su llave")
def main():
    opciones()
    try:
        option = int(input("Seleccione una opcion: "))
        frase = "Hola mundo hermoso"
        if  option <1 or option >5:
            print("Recuerde que las opciones son entre el 1-5...")
            return
        
        match option:
            case 1:
                for v, cant in contar_vocales(frase).items():
                    print(f"{v}: {cant}")
            case 2:
                print("Metodo tradicional de ordenar en diccionario")
                for v, cant in dictionary_elem_order(contar_vocales(frase)).items():
                        print(f"{v}: {cant}")
            case 3:
                print("Metodo optimizado de ordenar en diccionario")
                for v, cant in optimo_dictionary_elem_order(contar_vocales(frase)).items():
                    print(f"{v}: {cant}")
            case 4:
                dictionary = {}
                if es_diccionario_vacio(dictionary):
                    print("Diccionario vacio")
                else:
                    print("Diccionario lleno!!!")
            case 5:
                vocal = input("Digame la llave: ")
                elemento = key_search(vocal,contar_vocales(frase))
                if elemento:
                    print(f"Elemento encontrado: {elemento}")
                else:
                    print("Elemento no encontrado!")
                
    except:
      print('An exception occurred')
    
                
if __name__=="__main__":
    main()