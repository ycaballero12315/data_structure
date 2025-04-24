from collections import Counter
from typing import List, Tuple, Any

def elem_most_communt(elemts:List[Tuple[Any, ...]])-> Tuple[Any,int]:
    counter = Counter(key for key, _ in elemnts)
    most_communt = counter.most_common(1)[0]
    return most_communt

if __name__ == '__main__':
    elemnts = [(2,3), (2,5), (6,3), (2,3), (2,5), (6,3), (2,3), (2,5), (6,3)]
    print(f"Tupla mas comun: {elem_most_communt(elemnts)}")
