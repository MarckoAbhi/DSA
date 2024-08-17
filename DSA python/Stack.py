class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack contents:")
            for item in self.items[::-1]:
                print(item)

# Create a stack
stack = Stack()

# Push elements onto the stack
stack.push(1)
stack.push(2)
stack.push(3)

# Display the stack
stack.display()

# Pop elements from the stack
popped_item = stack.pop()
if popped_item is not None:
    print(f"Popped item: {popped_item}")

# Display the updated stack
stack.display()
