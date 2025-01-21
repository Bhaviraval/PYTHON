def straightline():
    x1=int(input("enter a number x1"))
    x2=int(input("enter a number x2"))
    x3=int(input("enter a number x3"))
    y1=int(input("enter a number y1"))
    y2=int(input("enter a number y2"))
    y3=int(input("enter a number y3"))
    if y2-y1/x2-x1==y3-y2/x3-x2:
        print("the points lie on the same line")
    else:
        print("the points do not lie on the same line")
straightline()
    
           
