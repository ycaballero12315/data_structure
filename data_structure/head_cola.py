#to implement heap queue
import heapq
from typing import List

elems = [4,5,8,2,4]
heapq.heapify(elems)
    


if __name__ == "__main__":
    print(elems)
    
    #Elemento agregado
    heapq.heappush(elems, 89)
    print(elems)
    
    #Elemento eliminado
    heapq.heappop(elems)
    print(elems)