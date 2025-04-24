class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class listSE:
    def __init__(self):
        self.head = None
    
    def printList(self):
        tmp = self.head
        result = []
        while tmp:
            result.append(tmp.data)
            tmp = tmp.next
        return result

if __name__ == '__main__':
    lista = listSE()
    node1 = Node(45)
    node2 = Node(56)
    node3 = Node(78)
    lista.head = node1
    node1.next = node2
    node2.next = node3
    lista_se = lista.printList()
    print(lista_se)