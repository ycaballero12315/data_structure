from typing import List
from collections import Counter

def most_commun_elm(lst:List[int])->any:
    count = Counter(lst)
    return count.most_common(1)[0][0]

lst = [3,5,6,7,8,9,8,7,6,7]

print(f"Element most communt in the list: {most_commun_elm(lst)}")