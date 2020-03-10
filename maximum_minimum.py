a,b,c=input("Enter three numbers").split()
print(a,b,c)

if (a>b and b>c):
    print("a is maximum")
    print("c is minimum")
elif (b>a and a>c):
    print("b is maximum")
    print("c is minimum")
else :
    print("c is maximum")

    #print("a is minimum")
