from AreaPerimeterFunctions import *
while[True]:
    print("\n1.circle")
    print("\n2.cuboid")
    print("\n3.sphere")
    print("\n4.quit")
    choice=int(input("enter choice:"))
    if(choice==1):
        r1=int(input("enter radius:"))
        area=circlearea(r1)
        print("\narea is :"+str(area))
        perimeter=circleperimeter(r1)
        print("\nperimeter is:"+str(perimeter))
    elif(choice==2):
        l1=int(input("enter length:"))
        w1=int(input("enter width:"))
        h1=int(input("enter height:"))
        area=cuboidarea(l1,w1,h1)
        print("\n area is:"+str(area))
        perimeter=cuboidperimeter(l1,w1,h1)
        print("\n perimeter is:"+str(perimeter))
    elif(choice==3):
        r1=int(input("enter radius:"))
        area=spherearea(r1)
        print("n area is:"+str(area))
        perimeter=sphereperimeter(r1)
        print("\n perimeter is:"+str(perimeter))
    elif(choice==4):
        quit(0)
    else:
        print("give a valid choice")
