#insert a new node after the given prev_node
class Node:
# def insertafter(self, prev_node, new_node):
    #if prev_node is None :
    #    print("the given previous node must in linkedlist.")
   #     return
   # new_node = Node(New_data)
  #  new_node.next = prev_node.next
 #   prev_node.next = new_node
    
        
        # This function is in LinkedList class
# Function to insert a new node at the beginning
 def push(self, new_data):

	# 1 & 2: Allocate the Node &
	# Put in the data
    new_node = Node(new_data)

	# 3. Make next of new Node as head
    new_node.next = self.head

	# 4. Move the head to point to new Node
    self.head = new_node
