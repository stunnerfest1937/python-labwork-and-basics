text = input( "enter a string  ")
print(text[::-1])
C = 0

for i in range(len(text)):
    if text[i] == "a":
        break 

print("the last occurence of a is "  , len(text)-i)

   


