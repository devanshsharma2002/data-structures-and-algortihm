strin="i am devansh"
newstrin=""

s = strin.split(' ')
for words in s:
    newstrin=words+' '+newstrin
print(newstrin)

#reverse word order seperated by dots

word='devansh'
newword=""
for char in word:
    newword=char+'.'+newword

print(newword[:-1])

#aabbbcc->s2b3c2

abc="aabbbcc"
i=0
newabc=""
l=[]
count = 1

j=0
for i in range(1,len(abc)):
    if abc[i-1]==abc[i]:
        count+=1
    else:
        newabc+=abc[j]
        newabc+=str(count)
        j=i
        count=1
newabc+=abc[j]
newabc+=str(count)

print(newabc)

#string to int

stringint='12345'
i=len(stringint)
integer=0
hashma={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
for j in range(0,i):
    digit=hashma[stringint[j]]
    print(digit,i-j)
    integer=digit*(10**(i-j-1))+integer
    print(integer)
print(integer)

#detect any non repeated char presence

a='aabbccdddef'
setc=set(a)
for i in setc:
    print(i)
print(setc)

#count character
a1='aabbccdddef'
dic=dict()
for char in a1:
    if char in dic:
        dic[char]=dic[char]+1
    else: 
        dic[char]=1
#find char with count =2 
print(dic)
i=0
for lor in dic:
    if dic[lor]==1:
        print(lor)
cas=3
print(a1.is)



    



    


