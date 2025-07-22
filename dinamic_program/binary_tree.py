# A Python class that represents an individual node
# in a Binary Tree

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def printInOrder(root):
    if root:
        printInOrder(root.left)
        print(root.data)
        printInOrder(root.right)

def printPostOrder(root):
    if root:
        printPostOrder(root.left)
        printPostOrder(root.right)
        print(root.data)

def printPreOrder(root):
    if root:
        print(root.data)
        printPreOrder(root.left)
        printPreOrder(root.right)
    
if __name__ == "__main__":
    root = Node(4)
    root.left = Node(6)
    root.right = Node(20)  
    root.left.left = Node(60)
    root.left.right = Node(80)
    root.right.left = Node(40)
    root.right.right = Node(100)
    print('\n In Order')
    printInOrder(root)
    print('___________________')
    print('___Postorder___')
    print(printPostOrder(root))
    print('___Preorder___')
    print(printPreOrder(root))
    
    
    