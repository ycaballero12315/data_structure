from datetime import datetime

class Ventas:
    def __init__(self):
        self.registro_ventas = {}

    def registrar_ventas_efectuadas(self, fecha, detalles_producto):
        fecha_str = fecha.strftime("%d-%m-%Y")
        self.registro_ventas[fecha_str] = detalles_producto
    
    def obtener_fecha(self):
        while True:
            entrada = input("Ingrese una fecha (formato DD-MM-YYYY): ")
            try: 
                fecha = datetime.strptime(entrada, "%d-%m-%Y")
                print(f"Fecha válida: {fecha.date()}")
                return fecha
            except ValueError:
                print("Formato incorrecto")

    def imprimir_ventas(self):
        if not self.registro_ventas:
            print("No existen registros de ventas")
        else:
            for fecha, detalles in self.registro_ventas.items():
                producto = detalles["producto"]
                cantidad = detalles["cantidad"]
                precio_producto = detalles["precio"]
                total = cantidad * precio_producto

                print(f"Fecha: {fecha}| Producto: {producto} | Cantidad: {cantidad} \n" 
                    f"Precio Unitario: {precio_producto:.2f} | Total: {total:.2f}")

def solicitar_dato(tipo, mensaje, error_mensaje, condicion=lambda x: x > 0):
    """
    Función genérica para solicitar y validar datos.
    :param tipo: Tipo al que se debe convertir el dato (int o float).
    :param mensaje: Mensaje mostrado al usuario.
    :param error_mensaje: Mensaje mostrado en caso de error.
    :param condicion: Función que evalúa si el valor es válido.
    :return: Valor válido ingresado por el usuario.
    """
    while True:
        try:
            valor = tipo(input(mensaje))
            if not condicion(valor):
                raise ValueError(error_mensaje)
            return valor
        except ValueError as e:
            print(f"Entrada inválida: {e}")

def main():
    venta = Ventas()

    while True:
        fecha = venta.obtener_fecha()
        producto = input("Producto vendido: ")
        
        # Solicitar cantidad y precio usando la función genérica
        cantidad = solicitar_dato(
            int, 
            "Cantidad de productos a registrar: ", 
            "La cantidad debe ser un número entero mayor a 0."
        )
        precio_producto = solicitar_dato(
            float, 
            "Precio del producto: ", 
            "El precio debe ser un número mayor a 0."
        )

        detalles_producto = {
            'producto': producto,
            'cantidad': cantidad,
            "precio": precio_producto
        }

        venta.registrar_ventas_efectuadas(fecha, detalles_producto)

        option = input("Registar otra venta (s/n): ").lower().strip()
        if option != "s":
            break

    venta.imprimir_ventas()

if __name__== "__main__":
    main()