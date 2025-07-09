from collections import Counter


test = [4,3,6,7,89]

print(test[::-1])
print(sorted(test, reverse=True))

myDict = {elem: elem - 1 for elem in test}
print(myDict)

all_list = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']

convert_set = set(all_list)

for i in convert_set:
    print(f"Elemento: {i}\n", end = " ")
    
count = Counter([3,4,5,3,4,5,3,4,5])

print(count)
count.update([3])
print(count)