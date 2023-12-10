class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.is_empty():
            new_node.next = new_node  # Point to itself for a single node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            new_node.next = new_node  # Point to itself for a single node
            self.head = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def delete_at_beginning(self):
        if not self.is_empty():
            if self.head.next == self.head:
                self.head = None
            else:
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                temp.next = self.head.next
                self.head = self.head.next
        else:
            print("Circular linked list is empty. Cannot delete.")

    def delete_at_end(self):
        if not self.is_empty():
            if self.head.next == self.head:
                self.head = None
            else:
                temp = self.head
                prev = None
                while temp.next != self.head:
                    prev = temp
                    temp = temp.next
                prev.next = self.head
        else:
            print("Circular linked list is empty. so it  Cannot delete.")

    def display(self):
        if not self.is_empty():
            temp = self.head
            while True:
                print(temp.data, end=" ==> ")
                temp = temp.next
                if temp == self.head:
                    break
            print(" (head)")
        else:
            print("Circular linked list is empty.")

# Example usage
if __name__ == "__main__":
    my_circular_list = CircularLinkedList()

    my_circular_list.insert_at_beginning(10)
    my_circular_list.insert_at_beginning(5)
    my_circular_list.insert_at_end(20)
    my_circular_list.display()

    my_circular_list.delete_at_beginning()
    my_circular_list.display()

    my_circular_list.delete_at_end()
    my_circular_list.display()









# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next_node = None

# class CircularLinkedList:
#     def __init__(self):
#         self.head = None

#     def insert(self, data):
#         new_node = Node(data)
#         if not self.head:
#             # If the list is empty, make the new node the head and point it to itself
#             self.head = new_node
#             new_node.next_node = self.head
#         else:
#             # Find the last node and update its next_node to the new node
#             current = self.head
#             while current.next_node != self.head:
#                 current = current.next_node
#             current.next_node = new_node
#             # Update the new node's next_node to the head to form the circular link
#             new_node.next_node = self.head

#     def display(self):
#         if not self.head:
#             print("Circular Linked List is empty.")
#             return

#         n = self.head
#         while True:
#             print(n.data, end=" ==> ")
#             n = n.next_node
#             if n == self.head:
#                 break
#         print("(Back to the beginning)")

# # Creating a circular linked list with the given elements
# elements = [50, 90, 130, 70, 150, 210, 170, 240, 300]

# circular_linked_list = CircularLinkedList()
# for element in elements:
#     circular_linked_list.insert(element)

# # Displaying the circular linked list
# circular_linked_list.display()
