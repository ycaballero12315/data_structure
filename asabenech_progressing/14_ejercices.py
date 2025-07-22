def escribircentrado(texto):
    ancho = 80
    espacios = ((ancho - len(texto))//2)
    print(" " * espacios + texto)
    print(" " * espacios + "=" * len(texto))

texto = input("Digame el texto que quiere centar: ")
escribircentrado(texto)