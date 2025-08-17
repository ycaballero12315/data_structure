import pandas as pd
import numpy as np
import regex as rg

class Foo:
    def __init__(self, x):
        self.x = x

    def test(self):
        return "Foo: {}".format(self.x)


class Bar:
    def __init__(self, x):
        self.x = x

    def test(self):
        return "Bar: {}".format(self.x)


class Foobar(Foo, Bar):
    pass


obj = Foobar(10)
print(obj.test())

def Mult(b:int, c: int)->int:
    try:
        return b/c
    except ZeroDivisionError as e:
        return 0
    else:
        return 1

print(Mult(9,10))

dictionary = {'id': [54, np.nan, np.nan, 34, 56, np.nan],
              'name': ['yoeny', 'dunieska', 'samu', 'sofia', np.nan, 'nelson'],
              'precios': [45.6, 67.8, 78.56, np.nan, np.nan, np.nan]}

try:
    df = pd.DataFrame(dictionary)
    print(df.isnull().sum())
except ValueError as v:
    print(f'Error en el calculo del DataFrame {v}')
else:
    print(df[df.isnull().any(axis=1)])

text = 'D t C mpBl ckFrid yS le'
elem = 'a'
new_text = ''
for i in text:
    new_text += elem if i == " " else i
        

print(new_text)

new_elem = ['a']* len(text)
new_str = ''.join(new if origin == ' ' else origin for origin, new in zip(text,new_elem))

new_new_str = ''.join('a' if ch == " " else ch for ch in text)

nuevo_texto = ''
for idx, elm in enumerate(text):
    nuevo_texto += 'a' if elm == " " else elm 

nuevo_texto_test = ['a' if ch == ' ' else ch for idex, ch in enumerate(text)]      

print(f'Sustitucion de texto con expresiones regulares: {rg.sub(r"(?<=\w)\s(?=\w)", 'a', text)}')
print(f'Despues de ser modificado con enumerate:{nuevo_texto}')
print(f"depues de ser modificado con enumerate pero usando compresion de lista: {nuevo_texto_test}")
print(new_str)
print(new_new_str)