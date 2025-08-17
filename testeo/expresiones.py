import re

mach_palagrafh = 'Hola hoy si voy a vencer'
other_elem = 'Yo no soy el elemento'

mach = re.match("Hola", mach_palagrafh, re.I)
mach = re.match("Hola", other_elem, re.I)

if not(mach == None):

    end, back = mach.span()
    print(mach_palagrafh[end:back])
else:
    print('No mache')

findall = re.findall('si', mach_palagrafh, re.I)
print(findall)

pattern = r'[Yy]|soy|voy'
findall = re.findall(pattern, mach_palagrafh)
search = re.search(pattern, mach_palagrafh)
pattern = r'[Y].*'
findall = re.findall(pattern, mach_palagrafh) 
print(findall)
print(search)
print(mach_palagrafh[7:8])

email = 'encontre el email ahora si yoenycaballerogonzalez@gmail.com'
pattern = r'[a-zA-Z0-9_.%+-]+@[a-zA-Z0-9_.-]+\.[a-zA-Z]{2,}$'
findall = re.findall(pattern, email)
search = re.search(pattern, email)
init, end = search.span() if search else (None, None)
print('Email encontrado:', email[init:end] if init is not None else 'No se encontró un email válido')
print(search)
print(findall)
if findall:
    print('Email encontrado:', findall[0])