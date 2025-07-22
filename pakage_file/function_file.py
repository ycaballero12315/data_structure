path = './file/'
todos = []

def write_file(elems):
    try:
        """Funtion write file return None"""
        filename = input('Name of file create: ')
        with open(f'{path}{filename}', 'w') as ff:
            for item in todos:
                ff.write(item)
    except FileNotFoundError:
        print('No se puede leer el fichero')
        
def read_file():
    namefile = input('Name of file read: ')   
    
    try:
        with open(f'{path}{namefile}', 'r') as ff:
            lines = ff.readlines()
        return lines
                  
    except FileNotFoundError:
        print('No se puede leer el fichero')