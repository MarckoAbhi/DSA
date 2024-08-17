class Node:
    def __init__(self,data):
        self.data = data
        self.ref=None

class Linkedlist:
    def __init__(self):
        self.head = None
           # display the the  node   
    def display(self):
        if self.head is None:
            print("linked listis empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"==>",end=" ")
                n = n.ref             
# Function to insert a new node at the beginning
    def add_begin(self, data):
        new_node= Node(data)
        new_node.ref = self.head    # 3. Make next of new Node as head
        self.head = new_node          # 4. Move the head to point to new Node
# add at the end
    def add_end(self,data):
        new_node= Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n= n.ref
            n.ref=new_node
    #add any position
    def add_after(self, data,x):
        n = self.head
        while n is not None:
            if x ==n.data:
                break
            n=n.ref
        if n is None:
            print("node is not present in LL")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
    #delete ar begin
    def delete_begin(self):
        if self.head is None:
            print("LL is empty so we can't delete nodes! ")  
        else:
            self.head=self.head.ref      
    
LL1=Linkedlist()
LL1.add_begin(30)
LL1.add_begin(20)
LL1.add_begin(10)
LL1.add_begin(5)
LL1.add_end(120)
LL1.add_after(200,120)
LL1.delete_begin()
LL1.display()
