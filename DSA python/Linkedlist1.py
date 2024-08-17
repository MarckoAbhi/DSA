class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def display(self):
        n = self.head
        while n:
            print(n.data, end=" => ",)
            n = n.next_node
        print("Linked list is not empty")
        
    def find_middle(self):
        slow_pointer = self.head
        fast_pointer = self.head
        while fast_pointer is not None and fast_pointer.next_node is not None:
            fast_pointer = fast_pointer.next_node.next_node
            slow_pointer = slow_pointer.next_node
        return slow_pointer.data    

# Creating a linked list with the given elements
elements = [50, 90, 130, 70, 150, 210, 170, 240, 300,40]

linked_list = LinkedList()
for element in elements:
    linked_list.insert(element)

# Displaying the linked list
linked_list.display()
