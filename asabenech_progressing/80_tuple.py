from typing import Tuple, List
def del_dupli_list_tuplas(list_tuple: List[Tuple[int, str]], 
                          list_tuple2: List[Tuple[int, str]]
                          )-> List[Tuple[int, str]]:
    resul = {item[0]:item for item in list_tuple + list_tuple2}
    
    return list(resul.values())

list1 = [(1, 'a'), (2, 'b'), (3, 'c')]
list2 = [(2, 'd'), (4, 'e')]

print(del_dupli_list_tuplas(list1, list2))