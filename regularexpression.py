import re

string = input("enter the string to match the pattern\n")

if(re.search("^[a-z][0-9][0-9][a-z]",string)):
    print("perfect matched")
else:
    print("not matched")
