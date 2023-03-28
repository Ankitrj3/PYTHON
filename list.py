## pre define module
##import calendar
##print(calendar.month(2022,2))

##import keyword
##print(keyword.kwlist)

##exception handleing

##a=int(input("enter the first number"))
##b=int(input("enter the second number"))
##
##try:
##    c=a/b
##    print(c)
##except:
##    print("any number cannot divide by zero")
##finally:
##    print("thank u and visit again")

##a=input("enter the value in the list ")
##list=(a)
##print(list)

##list=[45,23,56,23,78,56]
##try:
##    a=int(input("enter the value to find the number in the list\n"))
##    b=list.index(a)
##    print('your element is in index number',b)
##
##except:
##    print("your reponse is not found in the list")

##bob=[34,56,7,89,55,43]
##lis=input("enter the value to add the one or more element in list")
##bob.extend([lis])
##print(bob)

##list=[1,2,34,55,23]
##list.extend(['ankit','robin','ranjan'])
##print(list)


##list2=[23,45,67,34,23]
####ank=[int(input("enter")) for i in range(10)]
##arr = input("enter the numbers ")
##arr2 = arr.split(",")
##for i in range(len(arr2)):
##    arr2[i] = int(arr2[i])
##list2.extend(arr2)
##print(list2)

    

##finally:
##    print(list2.sort())
##    print(list2.count(67))
##    print(list2.index(4))
##    print(list2.pop())
##    print(list2.reverse())
##    print(type(list2))


lis=[1,2,3,4,5,6]
a=input("enter numbers in the list to extend the list")
a.split(',')
lis.extend(a)
print(lis)





















































