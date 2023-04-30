a=[]
size=int(input("enter the size of list\n"))
for i in range(size):
    value=int(input("enter the elements in the list\n"))
    a.append(value)

for i in range(size):
    a.reverse()
    
print("reverse",a)
    
