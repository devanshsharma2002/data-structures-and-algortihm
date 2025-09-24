class stack:
    def __init__(self):
        self.vals=list()
    def __str__(self):
        if not self.vals:
            return 'Empty STACK'
        else:
            string=''
            for i in self.vals:
                string=str(i)+'<=>'+string
            return string[:-3]+'||'


    def push(self, element):
        
        self.vals.append(element)
    def pop(self):
        if not self.vals:
            return 'Empty STACK'
        else:
            return self.vals.pop()

ob=stack()

ob.push(1)
ob.push(2)
ob.push(3)
ob.push(4)
print(ob)
ob.pop()

print(ob)
ob.pop()
print(ob)
ob.pop()
print(ob)
ob.pop()
print(ob)
ob.pop()


