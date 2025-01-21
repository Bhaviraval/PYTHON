def LeapYear():
    year=int(input("enter the year"))
    if year%400==0:
        if year%100==0:
            if year%4==0:
                print("the year is leap year")
    else:
        print("the year is not leap year")
LeapYear()
    
