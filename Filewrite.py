line1="THE TREE ARE GREEN"
file=input("enter file name")
f1=open(file,"w")
f1.write(line1)
f1.close()
f1=open(file,"r")
line=f1.read()
print("line",line)
f1.close()
