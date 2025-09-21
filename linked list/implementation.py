class node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LingLis:
    def __init__(self):
        self.num=0
        self.head=None
    def __len__(self):
        return self.num
    def __str__(self):
        cur= self.head
        strin=""
        while cur!=None:
            strin=cur.data+strin
            cur=cur.next

    def traversal(self):
        cur=self.head
        while cur!=None:
            print(cur.data)
            cur=cur.next
    def insertHead(self,data):
        new_node = node(data)
        new_node.next=self.head
        self.head=new_node
        self.num+=1
    


l=LingLis()
l.insertHead(1)
l.insertHead(2)
l.insertHead(3)
l.insertHead(4)
l.traversal()

