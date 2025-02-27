se=set()
while len(se)<6:
    b=input("enter the name =")
    se.add(b)
print(se)
nm=input("enter name you want to remove = ")
if nm in se:
    se.remove(nm)
    ad=input("enter the new name = ")
    se.add(ad)
print(se.pop(),"is remove")
print(se.pop(),"is remove")

print("after delet the two numbere",set(se))

