##user define functions
def calculations(a,b):
    print('add', a+b)
    print('sub', a-b)
    print('mul', a*b)
    print('div', a/b)
    print('mod', a%b)

calculations(23,12)

def sp(p,r,t):
    print('amount in rupees',p*r*t)

sp(1200,3,5)

def student():
   username=input("enter your user name\n")
   id=int(input("enter your registered id\n"))
   m1=int(input("enter your first subject marks\n"))
   m2=int(input("enter your second subject marks\n"))
   m3=int(input("enter your third subject marks\n"))
   m4=int(input("enter your fourth subject marks\n"))
   result=(m1+m2+m3+m4)/400
   percentage=result*100
   print(percentage, '% you got')

student()


