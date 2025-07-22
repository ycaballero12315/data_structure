def superposicion(frase, frase2):
    for f in frase:
        if f in frase2:
            found = True
            break
    if found:
        response = "Elemento se encuentra"
    else:
        response = "Elemento no encuentrado"
    return response

def superposicion_ani(phase, phase1):
    for i in phase:
        for j in phase1:
            if i == j:
                return True
                break
    return False
            
            
def main():
    frase = input("Frase uno: ")
    frase1 = input("Frase dos: ")
    print(superposicion(frase, frase1))
    print(superposicion_ani(frase, frase1))

if __name__ == "__main__":
    main()
    