#Count words in a sentence.
sentence=input("Enter Sentence: ")
words=sentence.split()

print("Number of words:",len(words))

# Find the longest word in a sentence.
sentence=input("Enter Sentence: ")
longest=""
words=sentence.split()

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)

# Remove all spaces from a string.
sentence=input("Enter Sentence: ")
after_remove=sentence.replace(" ","")

print(after_remove)

# Check whether two strings are equal.
s_1=input("Enter first string: ")
s_2=input("Enter second string: ")

if(s_1==s_2):
    print("Both are equal")
else:
    print("not equal")

# Count vowels and consonants separately
words=input("Enter words: ")
vowels=0
consonants=0

for char in words.lower():
    if char in "aeiou":
        vowels+=1
    elif char.isalpha():
        consonants+=1

print("Vowels:",vowels)
print("Consonants:",consonants)