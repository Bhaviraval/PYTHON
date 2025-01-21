def circle():
    r=int(input("enter the radius of the circle"))
    x=int(input("enter the x coordinate of the centre"))
    y=int(input("enter the y coordinate of the centre"))
    x1=int(input("enter the external x coordinate of the circle"))
    y1=int(input("enter the external y coordinate of the circle"))
    if x1*x1+y1*y1==r*r:
        print("the point lies on the circle")
    elif x1*x1+y1*y1<r*r:
        print("the point lies inside the circle")
    else:
        print("the number lies outside the circle")
circle()
