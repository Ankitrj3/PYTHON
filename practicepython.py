##list type
ank=[1,2,33,45,23,11,23]
ank.sort()
print(ank)
ank.pop()
print(ank)
ank.remove(33)
print(ank)
ank.reverse()
print(ank)
ank.remove(23)
print(ank)
ank.insert(2,56)
print(ank)
print(len(ank))
print(type(ank))
ank.insert(4,'ankitranjan')
print(ank)
liki=['a','b','c','d']
print(ank+liki)


##tuple type
i=(12,3,45,667,754,34)
l=(90,23,46,89,122)
print(i+l)
##i.insert(2,45)#it will give error because in tuple we can't edit the tuple
print(i.count(3))
print(type(i))
print(type(l))


##set type
i={12,23,44,56,7,8,67}
print(type(i))
##print(i.sort())# it will give error because set are unodered data type 
print(len(i))

## dictonary

i=[1,2,3,4]
j=['ank','liki','rj','sri']
print(dict(zip(i,j)))

ankit={'ank':1,'rj':2,'liki':3,'alla':4,'sri':5,'ranjan':6,7:{'a':'rob','b':'robin','c':'rk'}}

print(ankit)


















