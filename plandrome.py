string=input("enter the string to check wheather the string is plandrome\n")
string_word=string[::-1]
if(string==string_word):
    print(string,"is plandrome")
else:
    print(string,"is not plandrome")
