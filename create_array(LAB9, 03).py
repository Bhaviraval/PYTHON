def create_array(a,b,c,n):
    lc=[]
    for i in range(c):
        lc.append(n)
    lb=[lc]*b
    la=[lb]*a
    return la

print(create_array(3,4,5,7))
