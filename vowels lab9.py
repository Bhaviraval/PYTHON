def vowel(s):
    vowels='aeiouAEIOU'
    if len(s)==0:
        return 0
    else:
        if s[0] in vowels:
            return 1+vowel(s[1:])
    return vowel(s[1:])

str1=input("enter a string")
print(vowel(str1))
