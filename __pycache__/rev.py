i=int(input("enter a value  "))
reverse=0
while i>0:
    j=i%10
    reverse=reverse*10+j
    i=i//10
print("reversed value is " , reverse)
