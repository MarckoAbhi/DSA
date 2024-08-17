class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_end(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            new_node = Node(data)
            current.next = new_node
            new_node.prev = current

    def insert_after_node(self, key, data):
        current = self.head
        while current:
            if current.next is None and current.data == key:
                self.insert_end(data)
                return
            elif current.data == key:
                new_node = Node(data)
                new_node.prev = current
                new_node.next = current.next
                current.next.prev = new_node
                current.next = new_node
                return
            current = current.next

    def insert_before_node(self, key, data):
        current = self.head
        while current:
            if current.next is None and current.data == key:
                self.insert_beginning(data)
                return
            elif current.next.data == key:
                new_node = Node(data)
                new_node.prev = current
                new_node.next = current.next
                current.next.prev = new_node
                current.next = new_node
                return
            current = current.next

    def delete_at_end(self):
        if not self.is_empty():
            temp = self.head
            while temp.next:
                temp = temp.next
            if temp.prev:
                temp.prev.next = None
            else:
                self.head = None
            del temp
        else:
            print("Doubly linked list is empty. Cannot delete.")

    def delete_at_position(self, position):
        if not self.is_empty() and position > 0:
            temp = self.head
            for _ in range(position - 1):
                if temp is None:
                    print("Invalid position.")
                    return
                temp = temp.next
            if temp.prev:
                temp.prev.next = temp.next
            else:
                self.head = temp.next
            if temp.next:
                temp.next.prev = temp.prev
            del temp
        else:
            print("Doubly linked list is empty or invalid position. Cannot delete.")
            

dll = DoublyLinkedList()
dll.insert_beginning(5)
dll.insert_end(10)
dll.insert_after_node(5, 7)
dll.insert_before_node(10, 8)
dll.print_list()
print("after deleting beggining element list is:")
dll.delete_node(5)
dll.print_list()