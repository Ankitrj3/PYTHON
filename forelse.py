# lis=[]
# sum=0
# m=int(input("enter the size of the list\n"))
# for i  in range(m):
#       k=int(input("enter the values in list"))
#       lis.append(k)
# for i in range(len(lis)):
#        sum = sum+lis[i]
#
# print(sum)

nums=[12,3,16,26,44,33]

for num in nums:
      if num%5==0:
            print(num)
            break
else:
      print("not found number")

lis=[]
size=int(input("enter the size of the list\n"))
for i in range(size):
      k=int(input("enter the values in the list\n"))
      lis.append(k)
print(lis)
for li in lis:
      if(li%5==0):
            print(li,"the value is divisible by 5")
            break
else:
      print("the number is not divisible by 5 and number not found")