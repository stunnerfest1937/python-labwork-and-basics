text=input("enter the string")
dig=0
for char in text :
    if char in "0123456789"  :
        dig=dig+1

print("no of digits in string are" , dig  )
