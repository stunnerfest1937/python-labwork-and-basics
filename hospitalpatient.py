import random
c=0
d=0
e=0
f=0
for x in range(10):
    age=random.randint(1,100)
    print("patient age is ",age)
    body_temprature=random.randint(36,40)
    print("body temprature is  ", body_temprature)
    oxygen_saturation=random.randint(80,100)
    print("oxygen saturation is  ", oxygen_saturation)
    emergency=False
    eme=random.randint(1,2)
    if eme==1:
        emergency=True
        print("accident case ")
    else :
        print("non accident case")

    x=eme*body_temprature*oxygen_saturation*age
    if x>400000:
        print("patient priority is critical")
        c=c+1
    elif x>300000:
        print("patient priority is high")
        d=d+1
    elif x>200000:
        print("patient priority is moderate")
        e=e+1
    else :
        print("patient priority is normal")
        f=f+1





print ("no of critical patients is " , c)
print("no of high priority patients is " , d)
print("no of moderate priority pateints is " , e)
print("no of normal priority patients is " , f)