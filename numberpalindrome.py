# n=int(input("no of strings to be checked "))
# c=0
# d=0

# for x in range (n):
#   nostring=input("enter the string ")
#   i=(nostring[::-1])
#   if i==nostring :
#     print (" given no is palindrome")
#     c+=1
#   else :
#     print("given no isnt palindrome")
#     d+=1
# print("number of palindromes:",c)
# print("number of non-palindromes:",d)



n=int(input("enter how many strings to be checked  "))
temp=n
rev=0
c=0
d=0

for i in range (n) :
 numb=int(input("enter the three digit no  "))
  
while numb>0 :
    digit=numb%10
    rev=(rev*10)+digit
    numb=numb//10
 
    if rev==temp:
    
     c+=1

    elif rev!=temp :
    
      d+=1

print("no of palindromes :" , c)
print ("no of non palindromes :" , d)