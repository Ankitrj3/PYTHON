## user define classes
class Point():
    def getx(self):
        return self.x
## instances are the features of class like in the form of method , variable declaration
point1=Point() ## object declaration
point2=Point() ## object declaration

print(point1)
print(point2)
print(point1==point2)##checking that the object 1 equal to object 2
point1.x=5 ##assigning the values to point 1
point2.x=10##assigning the values to point 2
print(point1.getx())##printing the values of the object1
print(point2.getx())##printing the values of the object2

