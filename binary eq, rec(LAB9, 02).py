'''def binary(n,a):
    if n==0:
        return a
    a.append(n%2)
    return binary(n//2,a)

n=30
a=[]
binary(n,a)
c=
print(c)'''
def binary(n):
    if n:
       # print(n,n%2)
        #binary(n//2)
        return n%2+(10*binary(n//2))
    else:
        return n

n=30
print(binary(n))
