from collections import OrderedDict, defaultdict, ChainMap

od = OrderedDict()
od['a'] = 34
od['b'] = 56
od['c'] = 67

for k, e in od.items():
    print(f"\n {k}: {e}")

od['d'] = 89
for k, e in od.items():
    print(f"\n {k}: {e}")
    
df = defaultdict(int)    
L = [3,4,5,6,7,7,6,5,4]

for i, value in enumerate(L):
    df[i] += 1
    
for k, v in df.items():
    print(f'{k}:{v}')

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

ch = ChainMap(d1,d2,d3)
print(ch["a"])