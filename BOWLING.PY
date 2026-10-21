n=int(input("enter the number of pins"))
k=int(input("enter the number of balls"))
pins=[]
counter=0
while counter<n:
    pins+=["i"]
    counter+=1
ball=0
while ball<k:
    print("--- ball " , ball+1,"---")
    start=int(input("enter the starting pin number"))
    end=int(input("enter the ending pin number"))
    current_pin=start-1
    while current_pin<=end-1:
        pins[current_pin]="."
        current_pin+=1
    ball+=1
print("final state of pins is") 
for pin in pins:
    print(pin,end=" ")
print()

