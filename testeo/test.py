from typing import List, Dict

def factorial(n: int):
    if n < 0:
        raise ValueError('No existe el factorial para numeros menores de 0')
    elif n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

head = Node(7)
head.next = Node(9)
head.next.next = Node(10)

def print_node(head: Node):
    current = head
    while current:
        print(current.val)
        current = current.next

print_node(head)

class Node1:
    def __init__(self, val):
        self.val = val
        self.rigth = None
        self.left = None

class Binary_Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        def _insert(current, val):
            if current is None:
                return Node1(val)
            if val < current.val:
                current.left = _insert(current.left, val)
            else:
                current.rigth = _insert(current.rigth, val)
            return current
        
        self.root = _insert(self.root, val)
    
    def in_order(self):
        def _in_order(node: Node):
            while node:
                _in_order(node.left)
                print(node.val)
                _in_order(node.rigth)
            _in_order(self.root) 

def fibonassi(n, memo: dict = {}):
    if n in memo:
        return memo[n]
    if n < 0:
        raise ValueError("Error en el calculo de fibonassi")
    if n == 0 or n == 1:
        memo[n] = 1
    else:
        memo[n] = fibonassi(n-1, memo) + fibonassi(n-2, memo)
    return memo[n]

def fibo_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n+1)
    dp[1] = 1
    for elm in range(2, n+1):
        dp[elm] = dp[elm-1] + dp[elm-2]
    return dp[n]

def has_cycle(head):
    if not head and not head.next:
        return False
    fast = head
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
        
    return False 

def search_pto_beginning_cycle(head):
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None 

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow

if __name__ == "__main__":
    tree = Binary_Tree()
    for v in [4,5,6,7,8,9,10]:
        tree.insert(v)
    
    print(f'El fibonassi es {fibonassi(45)}')
    print(f'Este fibo es de la tabulacion {fibo_tab(45)}')
    print(tree.in_order())

