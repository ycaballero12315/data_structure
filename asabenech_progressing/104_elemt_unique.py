from typing import List, Set, Any

def delete_elem_unique_elm(elemt: List[Any])-> (Set[Any], List[Any]):
    unique_elem: Set[Any] = set()
    filter_elem: List[Any] = []
    
    for elem in  elemt:
        if elem not in unique_elem:
            unique_elem.add(elem)
            filter_elem.append(elem)
            
    return unique_elem, filter_elem


if __name__ == "__main__":
    elemnt = [4,5,6,4,6,7]
    collections_elem, list_elem = delete_elem_unique_elm(elemnt)
    print(f'la coleccion es: {collections_elem} y la lista no repetida es: {list_elem}')