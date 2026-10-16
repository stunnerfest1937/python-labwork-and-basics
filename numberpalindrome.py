n=int(input("no of strings to be checked"))

for x in range (n):
  nostring=input("enter the string")
  i=(nostring[::-1])
  if i==nostring :
    print (" given no is palindrome")
  else :
    print("given no isnt palindrome")

