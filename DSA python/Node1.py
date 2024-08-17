# insert new node at the beginning

#def push(self, new_data):
 #   new_node= Node(new_data)
  #  new_node.next = self.head
   # self.head = new_node
    
    
    
# Node class
class Node:

	# Function to initialize the node object
	def __init__(self, data):
		self.data = data # Assign data
		self.next = None # Initialize next as null

# Linked List class


class LinkedList:

	# Function to initialize the Linked List object
	def __init__(self):
		self.head = None
