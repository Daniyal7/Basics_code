year=int(input("Enter the year to find is leap year or not\n"))

if (year%4)==0:
    if(year%100)==0:
        if(year%400)==0:
            print(year,"is leap year")
        else:
            print(year,"Not leap year")
    else:
        print(year,"Not leap year")
else:
    print(year,"Not leap year")
