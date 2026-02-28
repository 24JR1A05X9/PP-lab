word = input("Enter a word: ")

vowels = "aeiouAEIOU"

for letter in word:
    if letter in vowels:
        print("The word contains a vowel.")
        break
else:
    print("The word does not contain any vowels.")
