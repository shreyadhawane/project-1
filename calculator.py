#calculator
a=int(input("enter the number"))
b=input("enter the operation mul/div/add/sub")
c=int(input("enter the second value"))

if b=="add":
    print(a+c)
elif b=="sub":
    print(a-c)
elif b=="mul":
    print(a*c)
elif b=="div":
    print(a/c)
else:
    print("operation not successful")

