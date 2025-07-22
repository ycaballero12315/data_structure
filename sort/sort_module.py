arr = [3,5,6,7,8,0]

arr = [int(i) for i in arr]


arr_sort = sorted(arr)


print(arr_sort)
elem = range(10)
print(elem)

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))

A3 = sorted([A0[s] for s in A0])

print(A3)