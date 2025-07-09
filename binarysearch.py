from typing import List, Any

def binary_rearch(elements:List[Any], elem:Any)-> Any:
    low, higt = 0, len(elements) -1
    
    while low <= higt:
      mid = (low + higt)//2
      
      if elements[mid] == elem:
          return f'El {elem} se encuentra en {mid + 1}'
      elif elements[mid]<elem:
          low = mid + 1
      else:
          higt = mid - 1
          
    return f'No se encuentra en la lista el elemento {elem}'

if __name__ == "__main__":
    elemnts = [10,50,70,56,78]
    print(f"{binary_rearch(elemnts, 10)}")
    print(f"{binary_rearch(elemnts, 78)}")
    print(f"{binary_rearch(elemnts, 70)}")