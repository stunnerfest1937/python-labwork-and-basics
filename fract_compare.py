a=int(input("Enter the numerator: "))
b=int(input("Enter the denominator: "))
if b==0:
    print("Denominator cannot be zero.")

c=int(input("enter the numerator of second fraction"))
d=int(input("enter the denominator of second fraction"))
if d==0:
    print("denominator cant be zero")

print ("first fraction is " , a/b)
print ("second fraction is " , c/d)
if (a*d)>(b*c):
    print("a/b is greater than c/d")
elif (c*b)>(a*d):
    print ("c/d is greater than a/b") 
else :
    print("both are equal")