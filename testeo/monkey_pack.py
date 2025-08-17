class Monkey_Parche:
    def monkey(elem):
       print(f'La suma de los elementos es: {sum(elem)}')

def monkey_parching(elems):
    print(f'La suma de los elementos es: {max(elems)}')


obj = Monkey_Parche()

obj.monkey = monkey_parching
obj.monkey([3,5,6,7,8,9])