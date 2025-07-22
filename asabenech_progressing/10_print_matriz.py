def print_patron():
    for _ in range(5):
        print('*'*10, end='\n')
print_patron()

print("___________________________________________")

def print_patron_aste():
    print('*' * 10)
    for _ in range(3):
        print('*'+ " " *8 + "*")
    print("*" * 10)
    # print("\n")

print_patron_aste()

print("____________________________________________")

def print_patron_creciente():
    cont = 1
    for _ in range(5):
        print('*' * cont)
        cont = cont + 1
    print('\n')

def print_patron_decre():
    cont = 5
    for _ in range(5):
        print('*' * cont)
        cont = cont - 1
    print('\n')


print_patron_creciente()
print_patron_decre()