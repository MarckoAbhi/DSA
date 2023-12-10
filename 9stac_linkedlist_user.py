class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.is_empty():
            popped_data = self.top.data
            self.top = self.top.next
            return popped_data
        else:
            print("Stack is empty.")
            return None

    def display(self):
        if not self.is_empty():
            current = self.top
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")
        else:
            print("Stack is empty.")

# Function to run stack operations by user input
def stack_operations():
    my_stack = StackLinkedList()

    while True:
        print("\nChoose an operation:")
        print("1. Display Stack")
        print("2. Push Element")
        print("3. Pop Element")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            my_stack.display()
        elif choice == "2":
            element = input("Enter the element to push: ")
            my_stack.push(element)
            print(f"{element} pushed onto the stack.")
        elif choice == "3":
            popped_element = my_stack.pop()
            if popped_element is not None:
                print(f"Popped element: {popped_element}")
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
  stack_operations()
