from collections import deque
from typing import List

def inversal_list(list_num:List[int])->List[int]:
    return list_num[::-1]

list_num = [4,5,6,7,8]

print(f"Lista invertida es: {inversal_list(list_num)}")