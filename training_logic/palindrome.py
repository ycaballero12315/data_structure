letter = input('Digame la frase:  ')

palindrome_l = 'Palindrome' if letter == letter[::-1] else "No palindrome"


print(palindrome_l)


