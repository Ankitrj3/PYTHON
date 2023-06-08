##break statement
# available=5
# x= int(input("how many candy u want ?"))
# i=1
# while i<=x:
#
#     if(i>available):
#         print("out of stock")
#         print("we available stock ",available)
#         break
#     print("candy")
#     i+=1
#
# print("thank you and visit again")

##continue statement
for i in range(1,10):
    if(i==3):
        continue

    print(i)
print("bye")

##pass statement

##printing only even numbers
# for i in range(1,101):
#     if(i%2!=0):
#         pass
#     else:
#         print(i)
#
# ##printing only odd numbers
# for i in range(1,101):
#     if(i%2==0):
#         pass
#     else:
#         print(i)