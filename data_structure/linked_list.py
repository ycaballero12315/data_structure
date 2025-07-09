class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None
    def add_node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def show_Linked_list(self):
        temp = self.head
        while temp:
            yield temp.data
            temp = temp.next
    def inverted_linked_list(self):
        prev = None
        current = self.head
        list_elm = []
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev     

llist = LinkedList()
llist.add_node(8)
llist.add_node(9)
llist.add_node(10)

print('Original List: ')
for elm in llist.show_Linked_list():
    print(f'{elm} -> ')
    
print('Inverted List: ')    
llist.inverted_linked_list()
for elm in llist.show_Linked_list():
    print(f'{elm} -> ')
    


    

    