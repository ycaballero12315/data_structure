import pickle
import os

data = {
    "name": "Yoeny",
    'last_name': 'Caballero',
    'cell': 58388827,
    'especiality': 'Software Ingenier', 
    'hibbies': ['read', 'Run', 'Program']
}

def create_binary_obj(data):
    try:
        with open('file/data.pkl', 'wb') as f:
            pickle.dump(data, f )
            print("Datos guardados!")
    except FileNotFoundError:
        print("Path no encontrado!!!")
        
def read_file_binary():
    try:
        if os.path.exists('file/data.pkl'):
            with open('file/data.pkl', 'rb') as f:
                file = pickle.load(f)
        return file
    except FileNotFoundError:
        print('File no encontrado')

create_binary_obj(data)

read_file = read_file_binary()
for k, v in read_file.items():
    if type(v) == list:
        print(v)