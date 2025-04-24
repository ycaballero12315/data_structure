def loggin(user, password):
    if user == "Login" and password == "asdasd":
        result = True
    else:
        result = False
    return result

if __name__ == "__main__":
    user = None
    password = None
    cont = 0
    while user != "Login" or password != "asdasd":
        user = input('Usuario: ')
        password = input("Contrasenna: ")
        cont = cont + 1
        if cont == 3:
            break
    else:
        loggin(user, password)
        print("Logging succefull!")
