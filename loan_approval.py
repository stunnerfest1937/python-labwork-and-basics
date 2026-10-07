c=0
d=0
import random
for x in range (10) :
 for i in range(1):
    age = random.randint(21, 65)
    print("age of the client is:", age)

    income = random.randint(20000, 100000)
    print("income of the client is : ", income)

    credit = random.randint(500, 800)
    print("credit score of client is : ", credit)

    amount = random.randint(100000, 1000000)
    print("amount of loan requested is  :", amount)

    if (income>40000) and (credit>650) and (amount<10*income) : 
      c=c+1
      print ("loan request accepted")
      
    else :
      print ("loan rejected")
      d=d+1

    print ("total no of clients is "  ,x+1)
    print ("total no approved clients are  " , c)
    print ("total no of rejected clients are " , d)
    print ("approval percentage is " , (c/(c+d))*100)
    



