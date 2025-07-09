from collections import Counter

element = ['B','B','A','B','C','A','B','B','A','C']

counter = Counter(element)
print(counter)

counter.update([x for x in ['A', 1] if isinstance(x, str)])
print(counter)