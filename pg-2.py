import random
se=set()
se1=set()
while(len(se)<11):
    b=random.randint(15,45)
    if(b not in se):
         se.add(b)
print(se)
c=0
for i in se:
    if(i<30):
        c=c+1
    if(i<=35):
        se1.add(i)
print("number less than 30 =",c)
print("number less then 35 == ",se1)
se=se1
print(se)
    
