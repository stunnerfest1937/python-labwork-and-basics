i=3
num=[1,2,4,5,8,10,22,3]
attempts=0
for n in num[:3]:
    attempts += 1
    if n==i:
        print("secret number found")
        break
    elif n>i:
        print("secret number is smaller than",n)
    else:
        print("secret number is greater than",n)
else:
    print("secret number was not found in the first 3 elements")
print("total number of attempts are",attempts)