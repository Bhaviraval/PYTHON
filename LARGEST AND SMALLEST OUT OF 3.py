def ls3():
    a=int(input("enter value of a"))
    b=int(input("enter value of b"))
    c=int(input("enter value of c"))
    lrg=a
    if b>lrg:
       lrg=b
    if c>lrg:
       lrg=c

    sml=a
    if b<sml:
       sml=b
    if c<sml:
       sml=c

    if lrg==sml:
        print("all values are same")
    else:
        print(lrg,"Largest",sml,"smallest")
ls3()
ls3()
        
