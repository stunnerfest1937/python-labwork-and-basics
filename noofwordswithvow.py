i=input("enter your sentence ")
words=i.split()
if words:
    count=0
    for word in words :
        if any(word.startswith(vowel) for vowel in "aeiouAEIOU"):
            count+=1
print ("the number of words starting with a vowel is", count)