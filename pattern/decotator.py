def decorator(f):
    def envoltura(*args, **kwargs):
        print('Este es primer msg')
        f(*args, **kwargs)
        print("Soy el fin")
        return f
    return envoltura


@decorator
def saludar(msg: str):       
    print(f"Hello {msg}")
    

saludar("Yoeny")