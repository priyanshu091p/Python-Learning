#Text Analyzer
'''Input:
Enter a sentence: Python is easy to learn

Output:
Characters: 23
Words: 5
Vowels: 8
Consonants: 12'''

sentence=input("Enter a  sentence: ")
vowels=0
consonants=0
words=sentence.split()

for char in sentence.lower():
    if char in "aeiou":
        vowels+=1
    elif char.isalpha():
        consonants+=1

print("Characters:",len(sentence))
print("Words:",len(words))
print("Vowels:",vowels)
print("Consonants:",consonants)