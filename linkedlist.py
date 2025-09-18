# creation of node class of linked list
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

#data is taken in as it would be needed each time
# linking of nodes will be done on runtime so it is not taken

#node creAtion
n1=node(40)
n2=node(30)
n3=node(10)

#linking
n1.next=n2
n2.next=n3

#traversal
def traversal(n)->node:
    current=n
    while current != None:
        print(current.data)
        current=current.next

#deletion
def deletionAtBeginning(head):
    current = head
    current.next=head
    return head

    
    
#addition
#at begin
initialnode=node(69)
initialnode.next=n1
deletionAtBeginning(initialnode)



# class for LL (CAMPUSX)

class LinkedList:
    def __init__(self):
        self.head=None
        self.num=0
    def __len__(self):
        return self.num
    def __str__(self):
        print("hi")
    def insert_head(self,data):
        #node creation
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node
        # this code works because python keeps the previous node as it is referenced by new node
        # and does not delete it until it is unreferenced.

        self.num+=1
    def traversal(self):
        curr_node=self.head
        while curr_node!=None:
            print(curr_node.data)
            curr_node=curr_node.next


L=LinkedList()
L.insert_head(69)
L.insert_head(68)
L.insert_head(67)
L.insert_head(66)
print(len(L))
L.traversal()
#note that trversal is in opposite oreder of insertion