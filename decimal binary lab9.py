def decimal_binary(n):
    if n>1:
        decimal_binary(n//2)
    print(n%2,end="")
num=int(input("enter a positive number:"))
decimal_binary(num)
