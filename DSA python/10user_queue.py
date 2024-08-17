class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        if not self.is_empty():
            print("Queue: ", end="")
            for item in reversed(self.items):
                print(item, end=" <- ")
            print("(Front)")
        else:
            print("Queue is empty.")

# Function to display the menu
def display_menu():
    print("\nQueue Operations:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

# Main program
queue = Queue()

while True:
    display_menu()
    choice = input("Enter your choice (1 to 4): ")

    if choice == "1":
        item = input("Enter the element to enqueue: ")
        queue.enqueue(item)
        print(f"{item} enqueued into the queue.")
    elif choice == "2":
        dequeued_item = queue.dequeue()
        if dequeued_item is not None:
            print(f"{dequeued_item} dequeued from the queue.")
        else:
            print("Queue is empty. Cannot dequeue.")
    elif choice == "3":
        queue.display()
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
