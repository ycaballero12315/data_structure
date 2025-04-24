from invertir import invertir

def palindrome(cadena):
    if cadena == invertir(cadena):
        result = "palindrome"
    else:
        result = "No palindrome"
    return result

print(palindrome("radar"))