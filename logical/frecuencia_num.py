from collections import Counter

N= 7
A = [4, 5, 2, 5, 2, 4, 4]

Counter(A).most_common(N)
# [(4, 3), (5, 2), (2, 2)]  
elem, rep = Counter(A).most_common(1)[0]
print(f'El elemento que mas se repite es: {elem}, y se repite {rep} veces')