balance=int(input("Enter the balance amount: "))
no=0
while balance>500:
    while no<6:
     import random
     withdrawal_amount = random.randint(100, 20000)
     if withdrawal_amount %100==0:
         balance=balance-withdrawal_amount
     no=no+1 

print("balance at day end is ", balance)

