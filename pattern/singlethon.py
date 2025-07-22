'''El singleton se usa para solamente tener una sola instancia por clase, \
    se puede usar en conexiones de base de datos \
        loggin, configuraciones globales, Pool de conexiones'''
        
        
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
    
class Logging(metaclass=SingletonMeta):
    def log(self, msg):
        print(f'[LOG]: {msg}')
        

logg1 = Logging()
logg2 = Logging()

print(logg1 is logg2)
logg2.log("Todos")