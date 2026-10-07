text = input("enter the word")
count = 0
for i in range(len(text)):
    if text[i] == "a" or text[i] == "e" or text[i] == "i" or text[i] == "o" or text[i] == "u":
        count = count + 1

print("no of vowels are  ", count)
print ("no of consonents are " , len(text)-count -1)