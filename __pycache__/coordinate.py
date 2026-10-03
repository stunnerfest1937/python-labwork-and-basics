x1=int(input("enter the value of x1 "))
y1=int(input("enter the value of y1 "))
print("coordinates of vertex a is ",x1 , y1)
x2=int(input("enter the value of x2 "))
y2=int(input("enter the value of y2 "))
print("coordinates of vertex b is ",x2 ,y2)
x3= int(input("enter the value of x3"))
y3=int(input("enter the value of y3 "))
print("coordinates of vertex c is ", x3 ,y3)

x4=0
y4=0

# since rectangle is parallel , x cords of opposite vertices are same and same for y
if x1==x2:
    x4=x3
elif x1==x3:
    x4=x2       

else:
    print ("x coordinates of opposite vertices are not same")

if y1==y2:
        y4=y3
elif y1==y3:
        y4=y2
else:
            print ("y coordinates of opposite vertices are not same")   



 
print("coordinates of vertex d is ",x4,y4)

