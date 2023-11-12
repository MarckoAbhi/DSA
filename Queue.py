class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def size(self):
        return len(self.items)

# Create a queue
queue = Queue()

# Enqueue elements
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# Dequeue elements
dequeued_item = queue.dequeue()
if dequeued_item is not None:
    print(f"Dequeued item: {dequeued_item}")

# Check the size of the queue
print(f"Queue size: {queue.size()}")

# Check if the queue is empty
print(f"Is the queue empty? {queue.is_empty()}")

