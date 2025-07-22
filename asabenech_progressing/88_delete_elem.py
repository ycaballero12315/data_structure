from typing import List

def delele_elem_repect(list_elem:List[int])-> List[int]:
    list_new = []
    for elem in list_elem:
        if elem not in list_new:
            list_new.append(elem)
    return list_new

def delete_elem_repect_compre(list_elem:List[int])-> List[int]:
    list_new = []
    [list_new.append(elem) for elem in list_elem if elem not in list_new]
    return list_new

def delete_elem_repect_dict(list_elem:List[int])-> List[int]:
    new_dict_elem = dict.fromkeys(list_elem)
    return list(new_dict_elem)    

list_elem = [5,7,8,9,9,5,7]

print(f"eliminar duplicados con dict: {delete_elem_repect_dict(list_elem)}")
print(f"eliminar duplicados con compresion: {delete_elem_repect_compre(list_elem)}")
print(f"eliminar duplicados con for: {delele_elem_repect(list_elem)}")

