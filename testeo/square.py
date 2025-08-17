import math as mat

def square_numebr(num: int)->bool:
    sq = int(mat.sqrt(num))
    check = sq ** 2 == num
    return check

print(square_numebr(9))

def factorial(n):
    if n < 0:
        return 0
    elif n == 1:
        return 1
    while n:
        return n* factorial(n-1)
    
fact = factorial(5)

def right_cero(fact):
    result = 0
    for i in str(fact)[::-1]:
        if int(i) == 0:
            result +=1
    return result

print(right_cero(fact))


def palabra_contenida_en_dictionary(palabra, list_palabras):
    for i in range(1, len(palabra)+1):
        first_srt = palabra[0:i]
        if first_srt in list_palabras:
            secund_str = palabra[i:0]
            if(
                not secund_str
                or secund_str in list_palabras
                or palabra_contenida_en_dictionary(secund_str, list_palabras)
            ):
                return True
    return False

s = 'yoenycaballero'
str_list = ['yoeny', 'caballero', 'gonzalez']

print(palabra_contenida_en_dictionary(s, str_list))


def removeDuplicates(array):
    size = len(array)
    insertIndex = 1
    for i in range(1, size):
        if array[i - 1] != array[i]:
            # Updating insertIndex in our main array
            array[insertIndex] = array[i]
            # Incrementing insertIndex count by 1
            insertIndex = insertIndex + 1
    return insertIndex

array_1 = [1,2,2,3,3,4]
removeDuplicates(array_1)