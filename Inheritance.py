class Publisher:
    def __init__(self,Pname):
        self.Pname=Pname
        def display(self):
            print("name",self.Pname)

class Book(Publisher):
    def __init__(self,Pname,Bname,title):
        self.Pname=Pname
        self.Bname=Bname
        self.title=title
    def display(self):
        print("Pname",self.Pname)
        print("Bname",self.Bname)
        print("title",self.title)
class Python(Book):
    def __init__(self,Pname,Bname,title,page,price):
     self.Pname=Pname
     self.Bname=Bname
     self.title=title
     self.page=page
     self.price=price
    def display(self):
        print("Pname:",self.Pname)
        print("Bname:",self.Bname)
        print("Title:",self.title)
        print("Pages:",self.page)
        print("Price:",self.price)
n=input("Enter Publisher:")
B=input("Enter Book:")
t=input("Enter Title:")
p=int(input("Enter Pages:"))
Pr=int(input("Enter Price:"))
obj=Python(n,B,t,p,Pr)
obj.display()
