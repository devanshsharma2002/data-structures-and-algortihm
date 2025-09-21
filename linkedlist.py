#todo
# error handling AND testing
# clear function repair
# 


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
        curr_node=self.head
        stroutp=''
        while curr_node!=None:
            stroutp=str(curr_node.data)+'->'+stroutp
            curr_node=curr_node.next

        return stroutp[:-2]
    def __getitem__(self,index):
        pass
    
    def insert_head(self,data):
        #node creation
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node
        # this code works because python keeps the previous node as it is referenced by new node
        # and does not delete it until it is unreferenced.

        self.num+=1
    def append(self,data):
        if self.head==None:
            return -1
        new_node=node(data)
        curr_node=self.head
        while curr_node.next!=None:
            curr_node=curr_node.next
        curr_node.next=new_node

        self.num+=1
    def insert_after(self,index,data):
        new_node=node(data)
        curr_node=self.head
        i=0
        if index>self.num:
            return -1
        while curr_node!=None:
            if i==index:
                curr_plus_one=curr_node.next
                curr_node.next=new_node
                new_node.next=curr_plus_one
            curr_node=curr_node.next
            i+=1
        self.num+=1

    def clear(self):
        self.head=0
        self.num=0
    def delete_head(self):
        curr_node=self.head
        self.head=curr_node.next
        self.num-=1
    def pop(self):
        curr_node=self.head
        while curr_node.next.next!=None:
            curr_node=curr_node.next
        curr_node.next=None
        self.num-=1
    def remove(self,item):
        if self.head.data==item:
            return self.delete_head()
            
        curr_node=self.head
        while curr_node.next!=None:
            
            if curr_node.next.data==item:
                curr_node.next=curr_node.next.next
            if curr_node.data==item:
                return self.pop()
            
            curr_node=curr_node.next
        self.num-=1
    
    def Search_by_value(self,value):
        pass
    def delete_by_index(self,index):
        pass
    def search_by_index(self,index):
        pass



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

L.insert_head('1')
print(L)
print(len(L))

L.append('69')
print(L)
print(len(L))


L.insert_after(0,100)
print(L)
print(len(L))

#L.clear()
#print(L)
#print(len(L))

L.delete_head()
print(L)
print(len(L))

L.pop()
print(L)
print(len(L))

L.remove(69)
print(L)
print(len(L))