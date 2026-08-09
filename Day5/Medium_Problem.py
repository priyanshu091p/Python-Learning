# Reverse a string.
name="Priyanshu"
print(name[::-1])

# Count vowels in a string.
name="Priyanshu"
count=0

for char in name:
    if char in "aeiou":
        count=count+1

print(f"Number of vowels : {count}")


#Count a particular character.
name="Priyanshu"
char=input("Enter character: ")

count=name.count(char)

print("Character appears:", count, "times")

# Replace spaces with -.
word="rgug urg sj uug urrrfrf"
print(word.replace(" ", "-"))

# Check whether a word is a palindrome.
word=input("Enter word: ")
reverse=word[::-1]
if(word==reverse):
    print("Word is palindrome")
else:
    print("word is not palindrome")