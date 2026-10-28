c=0
temp=0
x=0
i=int(input("enter the number to be checked"))
while i>0:
    d=i%10
    c=c+1
    i=i//10
    temp=i
    x=x+(temp*temp*temp)

print("the number of digits in the number is",c)   
if x==i:
    print("the number is an armstrong number")




      