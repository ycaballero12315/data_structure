from typing import List
import numpy as np

def split_list(list_elem: List[int], tamanno: int)-> List[List[int]]:
    
    return [list_elem[i:i+tamanno] for i in range(0, len(list_elem), tamanno)]

list_elem = [4, 6,7 ,8, 9,0, 4, 5, 6,7]
print(f"Las sublistas son {split_list(list_elem, 3)}")

result = np.array_split(list_elem, 3)

print([list(map(int, sublist)) for sublist in result])