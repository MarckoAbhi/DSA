class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.is_empty():
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def insert_at_position(self, data, position):
        if position < 1:
            print("Invalid position.")
            return
        new_node = Node(data)
        if position == 1:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return
        temp = self.head
        for _ in range(position - 2):
            if temp is None:
                print("Invalid position.")
                return
            temp = temp.next
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node

    def delete_at_beginning(self):
        if not self.is_empty():
            temp = self.head
            self.head = temp.next
            if self.head:
                self.head.prev = None
            del temp
        else:
            print("Doubly linked list is empty. Cannot delete.")

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

    def display(self):
        if not self.is_empty():
            temp = self.head
            while temp:
                print(temp.data, end=" <==> ")
                temp = temp.next
            print("None")
        else:
            print("Doubly linked list is empty.")

# Example usage
if __name__ == "__main__":
    dll = DoublyLinkedList()

    dll.insert_at_beginning(10)
    dll.insert_at_beginning(5)
    dll.insert_at_end(20)
    dll.insert_at_position(15, 2)
    dll.display()

    dll.delete_at_beginning()
    dll.display()

    dll.delete_at_end()
    dll.display()

    dll.delete_at_position(2)
    dll.display()
