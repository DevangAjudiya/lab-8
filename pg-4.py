se=set()
A=set()
B=set()
for i in range(6):
    s=input("enter the name =")
    se.add(s)
for i in se:
    if(i.startswith('A')):
       A.add(i)
    elif(i.startswith('B')):
         B.add(i)
print(A)
print(B)
       
