class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def get(self):
        return self.x
ob1=Point(1,2)
print(ob1.get())
