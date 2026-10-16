i=float(input("enter a number: "))
n=0
while i//10 != 0:
    i=i//10
    n=n+1
if n<1:
    print("the number is single digit")
elif n>=1:
    print("the number is double digit")
elif n>=100:
    print("the number is triple digit")
else:
    print("the number is more than triple digit")


