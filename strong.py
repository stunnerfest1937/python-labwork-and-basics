i=[1,2,3,4,5,6,7,8,9,145]
for x in i :
    d=0
    b=0
    temp=0
    d=i%10
    c=c+1
    i=i//10
    temp=i
    for z in (temp):
        b=b+(temp*(temp-1))
        temp=temp-1


if b==i:
    print ("the number is strong number")
else :
    print ("the number is not strong number")
       
       
