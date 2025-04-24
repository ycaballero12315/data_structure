def convert_seg(seg):
    horas = seg//3600 
    minut = (seg%3600)//60
    secund = seg % 60
    return horas, minut, secund

def horas_min_seg(hora, minuto, seg):
    return hora*3600+minuto*60+seg

def mostrar_menu():
    print("\nSeleccione una opción:")
    print("1. Convertir seg a horas, minutos y segundos: ")
    print("2. Convertir hora, min y seg a segundos: ")
    print("4. Salir")
    
def ejecutar_menu():
    mostrar_menu()
    option = input("Ingrese el numero de seleccion: ")
    
    match option:
        case '1':
            seg = int(input("Digame los segundos: "))
            print(f'La hora convertida es: {convert_seg(seg)}')
        case '2':
            hora = int(input("Digame la hora: "))
            minut = int(input("Digame los minutos: "))
            seg = int(input("Digame los segundos: "))
            print(f'La hora convertida es: {horas_min_seg(hora, minut, seg)}')

ejecutar_menu()          
    
    
    