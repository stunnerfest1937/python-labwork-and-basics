n=int(input("enter the total entries to be done"))
c=0
d=0
sum=0
for i in range (1,n+1):
    x=int(input("enter the no"))
    if x%3==0 and x%5==0:
        c+=1
    elif x%3==0 or x%5==0:
       d=d+1
       sum=sum+x

print("no of entries divisible by 3 or 5 are  " , d-c)
print ("sum is " , sum)
       