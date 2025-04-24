from collections import deque

de = deque([4,5,6,7,8,9,90])

de.popleft()
print(de)

for elm in de:
    print(elm)
    
del(de)