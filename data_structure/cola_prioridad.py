# A simple implementation of Priority Queue
# using Queue.
from typing import List

class PriorityQueue:
    def __init__(self)->None:
        self.queue: List[int] = []
        
    def __str__(self)->str:
        return ','.join([str(i) for i in self.queue])
    
    def insert(self, data)->None:
        self.queue.append(data)
    
    def isEmpty(self)-> bool:
        return len(self.queue) == 0
    
    def elemDelete(self)->int:
        if not self.isEmpty():
            try:
              max = 0
              for i in range(len(self.queue)):
                  if self.queue[i]>self.queue[max]:
                      max = i
              temp = self.queue[max]
              del self.queue[max]
              return temp
            except:
              exit()

if __name__ == "__main__":
    queue = PriorityQueue()
    queue.insert(45)
    queue.insert(60)
    queue.insert(100)
    queue.insert(1000)
    queue.insert(544444)
    
    print(queue)
    
    while not queue.isEmpty():
        print(queue.elemDelete())
    
    
