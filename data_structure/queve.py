from queue import LifoQueue

stack = LifoQueue(maxsize=5)

stack.put(10)
stack.put(20)
stack.put(40)
stack.put(60)
stack.put(100)

print(stack.qsize())
print(stack.full())

print(f'Last Elem: {stack.get()}')
print(stack.full())