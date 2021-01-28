lis=input("enter a list(space seperated):")
s1=lis.split()
print(s1)
result=''
for element in s1:
    result += str(element)
print("concatenate elements in the list:",result)
