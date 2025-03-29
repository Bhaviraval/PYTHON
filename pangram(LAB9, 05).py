def ispangram():
    alpha=("abcdefghijklmnopqrstuvwxyz")
    alpha+=alpha.upper()
    alpha_set=set(alpha)
    give=input("enter string: ")
    final=set(give)

    if alpha_set<=final:
        print("is pangram")
    else:
        print("not pangram")

ispangram()
