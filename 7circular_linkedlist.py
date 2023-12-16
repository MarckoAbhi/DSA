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
    
    
    def insert_at_position(self, pos, data):
        if pos <= 0:
            print("Insertion position must be greater than 0.")
            return

        if self.is_empty():
            print("Circular linked list is empty.")
            return

        new_node = Node(data)
        count = 1
        current = self.head
        while True:
            if count == pos:
                new_node.next = current.next
                current.next = new_node
                return
            count += 1
            current = current.next
            if current == self.head:
                break

        print("Given position is greater than the number of nodes.")
    
    
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
    
    
    def delete_from_position(self, pos):
        if pos <= 0:
            print("Deletion position must be greater than 0.")
            return

        if self.is_empty():
            print("Circular linked list is empty.")
            return

        count = 1
        current = self.head
        while True:
            if count == pos:
                prev = None
                temp = current
                while temp.next != self.head:
                    prev = temp
                    temp = temp.next
                prev.next = current.next
                return
            count += 1
            current = current.next
            if current == self.head:
                break

        print("Given position is greater than the number of nodes.")
    
    
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
    my_circular_list.insert_at_position(1,30)
    my_circular_list.insert_at_position(2,40) 
    my_circular_list.insert_at_position(3,50)
    my_circular_list.display()
    my_circular_list.delete_from_position(0)
    my_circular_list.display()
    
    
