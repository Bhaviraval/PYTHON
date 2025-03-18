def pfactors(n,i=2):
    if n==1:
        return[]
    if n%i==0:
        return[i]+pfactors(n//i,i)
    return pfactors(n,i+1)
null=int(input("write any positive integer:"))
print("prime factors of this number are:",pfactors(null))

