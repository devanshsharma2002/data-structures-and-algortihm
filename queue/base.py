class queue:
    def __init__(self):
        self.vals=list()
    def __str__(self):
        if not self.vals:
            return 'Empty QUEUE'
        else:
            string=''
            for i in self.vals:
                string=string+'<-'+str(i)
            return string[2:]

    def enqueue(self,elem):
        self.vals.append(elem)
    def dequeue(self):
        front=self.vals[0]
        self.vals=self.vals[1:]
        return front
    
ob=queue()
print(ob)

ob.enqueue(1)
ob.enqueue(1)
ob.enqueue(1)
ob.enqueue(1)
print(ob)
ob.dequeue()
ob.dequeue()
print(ob)

ob.dequeue()
print(ob)