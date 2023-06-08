fact=1
size=int(input("enter the value to find the factorial of the number\n"))
if(size<0):
    print("no factorial for negative numbers\n")
elif(size==0):
    print(("factorail of 0 is 1\n"))
else:
    for i in range(1,size+1):
        fact=fact*i
    print("the factorial of",i,"is",fact)