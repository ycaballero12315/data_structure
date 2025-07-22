def max_de_tres(uno, dos, tres):
    if uno > dos and uno > tres:
        result = uno
    elif dos > tres:
        result = dos
    else:
        result = tres
    return result

if __name__ == "__main__":
    uno = int(input("Primer numero: "))
    dos = int(input("Segundo numero: "))
    tres = int(input("Tercer numero: "))
    
    print(f"El numero mas grande entre {uno, dos, tres}: {max_de_tres(uno, dos, tres)}")
    
    
    