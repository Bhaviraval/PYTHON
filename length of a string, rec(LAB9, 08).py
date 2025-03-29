def length(l):
    if l=="":
        return 0
    else:
        return 1 + length(l[1: ])

a=input("enter string: ")
print(length(a))
