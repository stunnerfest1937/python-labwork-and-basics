import random
pin=random.randint(1000, 9999)
print("your pin is",pin)
x=0
correct=False
while x<3:
 i=int(input("enter your pin: "))
 if pin==i:
    print("correct pin ")
    correct=True
    break 
 else :
   print("incorrect pin , please try again ")
   x+=1
if not correct:
  print("you have exceeded the number of attempts ")
   
 

if pin==i:
  balance=random.randint(0,100000)
  print("your balance is ",balance)
  withdraw=int(input("enter the amount to withdraw "))
  if withdraw>balance:
    print("insufficient balance ")   
  else:
    balance=balance-withdraw
    print("withdraw successful ")
    print("your remaining balance is ",balance)



