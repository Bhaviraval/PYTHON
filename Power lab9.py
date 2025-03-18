def power(a,b):
    return 1 if b ==0 else a*power(a,b-1)

a=int(input("enter a value:"))
b=int(input("enter a power value:"))


print(a,"^",b,"=",power(a,b))
