class dynamic:
    def userinput(self,a,b):
        self.a=a
        self.b=b

    def calculation(self):
        self.a=int(input("enter the value 1 to do calculation\n"))
        self.b=int(input("enter the value 2 to do calculation\n"))
        return print("addition",self.a+self.b, "substraction",self.a-self.b, "division",self.a/self.b ," multiplication",self.a*self.b)

ob1= dynamic()

print(ob1.calculation())