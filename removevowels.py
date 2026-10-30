sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"

sentence_without_vowels = sentence.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "").replace("A", "").replace("E", "").replace("I", "").replace("O", "").replace("U", "")    
print("Sentence without vowels:", sentence_without_vowels)