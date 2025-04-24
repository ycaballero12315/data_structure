from collections import namedtuple

Student = namedtuple('Student', ['name', 'lastname', 'age'])

S = Student("Yoeny", 'Caballero', 41)

print(f'Su nombre es: {S.name}', end=' ')