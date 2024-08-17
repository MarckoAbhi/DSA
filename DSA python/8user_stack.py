class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty.")

    def display(self):
        if not self.is_empty():
            print("Stack:", self.items)
        else:
            print("Stack is empty.")

# Function to run stack operations by user input
def stack_operations():
    my_stack = Stack()

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
