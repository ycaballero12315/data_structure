def temp_media(t_min, t_max):
    return (t_min + t_max) / 2

if __name__ == "__main__":
    dias = int(input('Cantidad de dias: '))
    for i in range(1, dias+1):
        t_max = float(input("Temp Maxima: "))
        t_min = float(input("Temp Minima: "))
        print(f"El dia {i} habia una temp media de -> {temp_media(t_min, t_max)}")
