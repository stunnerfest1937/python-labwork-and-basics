n=int(input("enter the total entries to be done"))
c = 0
for i in range (1,n+1):
    is_prime = True
    for j in range (2,i):
        if i%j==0:
            is_prime = False
            break
    if is_prime:
        c+=1
        
        print(i) 
print("no of prime numbers are " , c)