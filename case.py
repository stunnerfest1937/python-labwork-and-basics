text=input("enter the string ")
uc=0
lc=0
for char in text :
    if char in "QWERTYUIOPASDFGHJKLZXCVBNM" :
        uc=uc+1

    if char in "qwertyuiopasdfghjklzxcvbnm" :
        lc=lc+1
print("no of uppercase letter are " , uc)
print("no of lowercase letters are "  , lc) 