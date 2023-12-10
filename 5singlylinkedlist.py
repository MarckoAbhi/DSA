class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
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

    def insert_at_position(self, data, position):
        if position < 1:
            print("Invalid position.")
            return
        new_node = Node(data)
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        for _ in range(position - 2):
            if temp is None:
                print("Invalid position.")
                return
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def delete_at_beginning(self):
        if not self.is_empty():
            temp = self.head
            self.head = temp.next
            del temp
        else:
            print("Singly linked list is empty. Cannot delete.")

    def delete_at_end(self):
        if not self.is_empty():
            temp = self.head
            prev = None
            while temp.next:
                prev = temp
                temp = temp.next
            if prev:
                prev.next = None
            else:
                self.head = None
            del temp
        else:
            print("Singly linked list is empty. Cannot delete.")

    def delete_at_position(self, position):
        if not self.is_empty() and position > 0:
            temp = self.head
            prev = None
            for _ in range(position - 1):
                if temp is None:
                    print("Invalid position.")
                    return
                prev = temp
                temp = temp.next
            if prev:
                prev.next = temp.next
            else:
                self.head = temp.next
            del temp
        else:
            print("Singly linked list is empty or invalid position. Cannot delete.")

    def display(self):
        if not self.is_empty():
            temp = self.head
            while temp:
                print(temp.data, end=" ==> ")
                temp = temp.next
            print("None")
        else:
            print("Singly linked list is empty.")

# Example usage
if __name__ == "__main__":
    sll = SinglyLinkedList()

    sll.insert_at_beginning(21)
    sll.insert_at_beginning(9)
    sll.insert_at_end(12)
    sll.insert_at_end(14)
    sll.insert_at_position(17, 3)
    sll.display()

    sll.delete_at_beginning()
    sll.display()

    sll.delete_at_end()
    sll.display()

    sll.delete_at_position(2)
    sll.display()
