i = input("enter your sentence ")
words = i.split()

if words:
    max_word = min(words, key=len)
    print("the shortest word is", max_word)
else:
    print("No words found.")




i = input("enter your sentence ")
words = i.split()

if words:
    max_word = max(words, key=len)
    print("the longest word is", max_word)
else:
    print("No words found.")
 