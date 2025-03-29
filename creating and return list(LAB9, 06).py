def tuple1(n):
    return[(x,x**2,x**3) for x in range(1,n+1)]

result=tuple1(7)
print(result)
