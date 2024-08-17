class Node:
    def __init__(self,data):
        self.data = data
        self.ref=None
        node1=Node(10)
        node2=Node(20)
        node3=Node(30)
        node4=Node(40)
               
# link node to each  other
        node1.ref=node2
        node2.ref=node3
        node3.ref=node4
 
class Linkedlist:
    def __init__(self):
        self.head = None
           # display the the  node   
    def display(self):
        if self.head is None:
            print("linked is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n = n.ref
LL1=Linkedlist()
LL1.display()
            
                
