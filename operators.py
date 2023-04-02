#assignment operator
a=12
b=45
c,d=30,89
print(a)
print(b)
print(c)
print(d)
a+=2
b+=4
c*=12
d-=2
print(a,b,c,d)

#arithmatic opertors
print(a+b,a-b,a*b,a/c,a%b)

#lambda function
x= lambda principal,rate,time:principal*rate*time
print(x(12000,23,2))

#logical operators and relational operator
if(a==b and b==c):
    print("equal")
else:
    print("not equal")

if(a<b or b<a):
    print('equal')
else:
    print('not equal')

if(a != b):
    print('equal')
else:
    print('not equal')

#creating a lambda functions using oprators and lambda funtions
# x= lambda a=int(input('enter val1')),b=int(input('enter val2')),c=int(input('enter val3')):a*b*c
# print(x())

#urinary operator
n=1
n=-1
print(n)

#urinary operator means assigning negative value to the variable

