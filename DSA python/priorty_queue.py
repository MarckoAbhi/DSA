class PriorityQueueNode:
    def __init__(self, value, pr):
        self.data = value
        self.priority = pr
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.front = None

    def isEmpty(self):
        return False if self.front else True

    def push(self, value, priority):
        if self.isEmpty():
            self.front = PriorityQueueNode(value, priority)
        else:
            newNode = PriorityQueueNode(value, priority)
            if self.front.priority < priority:
                newNode.next = self.front
                self.front = newNode
            else:
                temp = self.front
                while temp.next:
                    if priority >= temp.next.priority:
                        break
                    temp = temp.next
                newNode.next = temp.next
                temp.next = newNode

    def pop(self):
        if self.isEmpty():
            return None
        else:
            removed_node = self.front.data
            self.front = self.front.next
            return removed_node

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.front.data

    def traverse(self):
        if self.isEmpty():
            return "Queue is Empty!"
        else:
            temp = self.front
            while temp:
                print(temp.data,"==>", end=" ")
                temp = temp.next

def main():
    pq = PriorityQueue()
    pq.push(7, 1)
    pq.push(9, 2)
    pq.push(10, 3)
    pq.push(17, 0)

    print("\nQueue after push: ")
    pq.traverse()

    removed_highest_priority_item = pq.pop()
    print("\nRemoved highest priority item: ", removed_highest_priority_item)

    print("\nQueue after pop: ")
    pq.traverse()

if __name__ == "__main__":
    main()