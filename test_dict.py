from collections import OrderedDict, defaultdict


od = OrderedDict()

od["cepillo"] = 250
od["pasta"] = 1000
od["shampu"] = 1200


for k, d in od.items():
    print(f"{k}: {d}")

print("\n")
del od['shampu']
for k, d in od.items():
    print(f"{k}: {d}")
    
od["shampu"] = 1200

if 'shampu' in od.keys():
    od['shampu'] = 3000

for k, elm in od.items():
    print(f'{k}: {elm}')

dd = defaultdict(int)

L = [4,5,6,7,8,9]

for i in L:
    dd[i] = dd[i-1] + 1
    
for k, v in dd.items():
    print(f"{k}: {v}")
