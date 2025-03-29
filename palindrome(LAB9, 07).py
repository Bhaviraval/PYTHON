def is_pallindrome():
    string1=input("enter string: ")
    string1=string1.lower()
    for i in range(0,len(string1)//2):
        if (string1[i]!=string1[-1-i]):
            print("it is not pallindrome")
            break
    else:
        print("it is  pallindrome")
is_pallindrome()
