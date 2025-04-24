compras = [("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), 
          ("Jorge Russo", 7, 699, "Mirasol 218"), 
          ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), 
          ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), 
          ("Jorge Russo", 15, 958, "Mirasol 218")]

def direcciones_compra(compras):
    domicilios = set()
    clientes = set()
    dict_clientes = {}
    for co in compras:
        domicilios = co[3]
        clientes = co[0]
        
        dict_clientes[clientes] = domicilios
    return dict_clientes

def cliente_mas_compras(compras):
    
    cliente_num_compras = {}
    for compra in compras:
        cliente = compra[0]
        if cliente in cliente_num_compras:
            cliente_num_compras[cliente] += 1
        else:
            cliente_num_compras[cliente] = 1  

    cliente_top = None
    max_compras = 0
    
    for cliente, cantidad in cliente_num_compras.items():
        if cantidad > max_compras:
            cliente_top = cliente
            max_compras = cantidad
    return cliente_top, max_compras
        
print(direcciones_compra(compras))
print(f"El cliente top es: {cliente_mas_compras(compras)}")        