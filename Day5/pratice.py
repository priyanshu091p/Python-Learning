word = input("Enter a string: ")

count = {}

for char in word:
    if char != " ":
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

for char in count:
    print(char, "=", count[char])
    