# 📅 Day 5 – Python Strings 🐍

## 📚 Topics Covered

* What is a String?
* String Indexing
* Negative Indexing
* String Slicing
* `len()`
* `lower()` / `upper()`
* `strip()`
* `replace()`
* `find()`
* `count()`
* `split()`
* `join()`

---

# 📝 What is a String?

A string is a sequence of characters enclosed inside quotes.

Example:

```python
name = "Priyanshu"
message = 'Hello Python'
```

Strings can contain letters, numbers, spaces, and special characters.

---

# 🔢 String Indexing

Indexing is used to access individual characters from a string.

Python indexing starts from `0`.

Example:

```python
name = "Python"

print(name[0])
print(name[2])
```

Output:

```text
P
t
```

---

# 🔙 Negative Indexing

Negative indexing allows us to access characters from the end of a string.

Example:

```python
name = "Python"

print(name[-1])
print(name[-2])
```

Output:

```text
n
o
```

---

# ✂️ String Slicing

Slicing is used to get a part of a string.

### Syntax:

```python
string[start:stop]
```

Example:

```python
name = "Python"

print(name[0:3])
```

Output:

```text
Pyt
```

The `stop` index is not included.

---

# 📏 len()

The `len()` function returns the number of characters in a string.

Example:

```python
name = "Python"

print(len(name))
```

Output:

```text
6
```

---

# 🔠 lower() and upper()

### `lower()`

Converts all characters to lowercase.

```python
name = "PYTHON"

print(name.lower())
```

Output:

```text
python
```

### `upper()`

Converts all characters to uppercase.

```python
name = "python"

print(name.upper())
```

Output:

```text
PYTHON
```

---

# 🧹 strip()

`strip()` removes extra spaces from the beginning and end of a string.

Example:

```python
name = "  Python  "

print(name.strip())
```

Output:

```text
Python
```

---

# 🔄 replace()

`replace()` is used to replace one part of a string with another.

Example:

```python
text = "I like Java"

print(text.replace("Java", "Python"))
```

Output:

```text
I like Python
```

---

# 🔍 find()

`find()` returns the index of the first occurrence of a character or substring.

Example:

```python
text = "Python"

print(text.find("t"))
```

Output:

```text
2
```

---

# 🔢 count()

`count()` returns how many times a character or substring appears.

Example:

```python
text = "banana"

print(text.count("a"))
```

Output:

```text
3
```

---

# ✂️ split()

`split()` breaks a string into a list of words.

Example:

```python
text = "Python is easy"

print(text.split())
```

Output:

```text
['Python', 'is', 'easy']
```

---

# 🔗 join()

`join()` combines multiple strings into one string.

Example:

```python
words = ["Python", "is", "easy"]

result = " ".join(words)

print(result)
```

Output:

```text
Python is easy
```

---

# 💻 Practice Questions

## 🟢 Easy (1–5)

1. Take a name and print it.

2. Print the first and last character.

3. Find the length of a string.

4. Convert a string to uppercase.

5. Convert a string to lowercase.

---

## 🟡 Medium (6–10)

6. Reverse a string.

7. Count vowels in a string.

8. Count a particular character.

9. Replace spaces with `-`.

10. Check whether a word is a palindrome.

---

## 🔥 Challenge (11–15)

11. Count words in a sentence.

12. Find the longest word in a sentence.

13. Remove all spaces from a string.

14. Check whether two strings are equal.

15. Count vowels and consonants separately.

---

# 🚀 Mini Project

## Text Analyzer

Create a program that analyzes a sentence entered by the user.

### Input:

```text
Enter a sentence: Python is easy to learn
```

### Program should calculate:

* Number of characters
* Number of words
* Number of vowels
* Number of consonants

### Expected Output:

```text
Characters: 23
Words: 5
Vowels: 8
Consonants: 12
```

### Concepts Used:

* Strings
* `len()`
* `lower()`
* `split()`
* String indexing
* `count()`
* `for` loop
* Conditional statements

---

# 🛠️ Tools Used

* Python
* VS Code
* Git & GitHub

---

# 👨‍💻 Author

**Priyanshu**
