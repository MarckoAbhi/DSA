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
        print("Linked list is empty")

# Creating a linked list with the given elements
elements = [50, 90, 130, 70, 150, 210, 170, 240, 300,40]

linked_list = LinkedList()
for element in elements:
    linked_list.insert(element)

# Displaying the linked list
linked_list.display()
