n=int(input("number till which fibonacci is to be found"))
f0=0
f1=1
for i in range (n):
    print (f0)
    print (f1)
    
    f2=f1+f0
    print (f2)
    f1=f0
    f2=f1

