# 📅 Day 8 — Python Dictionaries 🔑

## 📚 Topics Covered

1. What is a Dictionary?
2. Creating a Dictionary
3. Key & Value
4. Accessing Values
5. Adding New Key-Value Pairs
6. Updating Existing Values
7. `len()`
8. `keys()`
9. `values()`
10. `items()`
11. `get()`
12. `pop()`
13. `del`
14. Checking Key Existence using `in`
15. Dictionary with `for` Loop
16. `max()`
17. `sum()`
18. Nested Dictionary — Basic
19. Dictionary with Lists
20. Character Frequency using Dictionary

---

# 📖 1. What is a Dictionary?

A dictionary stores data in **key-value pairs**.

Example:

```python
student = {
    "name": "Priyanshu",
    "course": "BCA",
    "marks": 85
}

print(student)
```

Output:

```text
{'name': 'Priyanshu', 'course': 'BCA', 'marks': 85}
```

---

# 📝 2. Creating a Dictionary

A dictionary is created using curly brackets `{}`.

```python
student = {
    "name": "Priyanshu",
    "age": 21,
    "course": "BCA"
}

print(student)
```

Output:

```text
{'name': 'Priyanshu', 'age': 21, 'course': 'BCA'}
```

---

# 🔑 3. Key & Value

Every dictionary item contains a **key** and its corresponding **value**.

```python
student = {
    "name": "Priyanshu",
    "marks": 85
}
```

Here:

* `"name"` → Key
* `"Priyanshu"` → Value
* `"marks"` → Key
* `85` → Value

---

# 🔍 4. Accessing Values

Values can be accessed using their keys.

```python
student = {
    "name": "Priyanshu",
    "marks": 85
}

print(student["name"])
print(student["marks"])
```

Output:

```text
Priyanshu
85
```

---

# ➕ 5. Adding New Key-Value Pairs

A new key-value pair can be added using a new key.

```python
student = {
    "name": "Priyanshu",
    "marks": 85
}

student["city"] = "Ghaziabad"

print(student)
```

Output:

```text
{'name': 'Priyanshu', 'marks': 85, 'city': 'Ghaziabad'}
```

---

# 🔄 6. Updating Existing Values

An existing value can be changed using its key.

```python
student = {
    "name": "Priyanshu",
    "marks": 85
}

student["marks"] = 90

print(student)
```

Output:

```text
{'name': 'Priyanshu', 'marks': 90}
```

---

# 📏 7. len()

`len()` returns the number of key-value pairs.

```python
student = {
    "name": "Priyanshu",
    "age": 21,
    "course": "BCA"
}

print(len(student))
```

Output:

```text
3
```

---

# 🔑 8. keys()

`keys()` returns all the keys.

```python
student = {
    "name": "Priyanshu",
    "age": 21,
    "course": "BCA"
}

print(student.keys())
```

Output:

```text
dict_keys(['name', 'age', 'course'])
```

---

# 💰 9. values()

`values()` returns all the values.

```python
student = {
    "name": "Priyanshu",
    "age": 21,
    "course": "BCA"
}

print(student.values())
```

Output:

```text
dict_values(['Priyanshu', 21, 'BCA'])
```

---

# 🔗 10. items()

`items()` returns all key-value pairs.

```python
student = {
    "name": "Priyanshu",
    "marks": 85
}

print(student.items())
```

Output:

```text
dict_items([('name', 'Priyanshu'), ('marks', 85)])
```

---

# 🔎 11. get()

`get()` is used to access a value using its key.

```python
student = {
    "name": "Priyanshu",
    "marks": 85
}

print(student.get("name"))
```

Output:

```text
Priyanshu
```

If the key does not exist, `get()` returns `None` instead of raising a `KeyError`.

```python
print(student.get("city"))
```

Output:

```text
None
```

---

# 🗑️ 12. pop()

`pop()` removes a key-value pair using its key.

```python
student = {
    "name": "Priyanshu",
    "marks": 85,
    "city": "Ghaziabad"
}

student.pop("city")

print(student)
```

Output:

```text
{'name': 'Priyanshu', 'marks': 85}
```

---

# ❌ 13. del

`del` can be used to delete a key-value pair.

```python
student = {
    "name": "Priyanshu",
    "marks": 85
}

del student["marks"]

print(student)
```

Output:

```text
{'name': 'Priyanshu'}
```

---

# 🔍 14. Checking Key Existence using `in`

The `in` operator checks whether a key exists.

```python
student = {
    "name": "Priyanshu",
    "marks": 85
}

print("name" in student)
print("city" in student)
```

Output:

```text
True
False
```

---

# 🔁 1 5. Dictionary with for Loop

A `for` loop can be used to iterate through a dictionary.

### Keys:

```python
student = {
    "name": "Priyanshu",
    "marks": 85
}

for key in student:
    print(key)
```

Output:

```text
name
marks
```

### Keys and Values:

```python
for key, value in student.items():
    print(key, value)
```

Output:

```text
name Priyanshu
marks 85
```

---

# 🔢 16. max()

`max()` can be used to find the highest value.

Example:

```python
marks = {
    "Aman": 75,
    "Rahul": 90,
    "Priyanshu": 85
}

highest = max(marks.values())

print(highest)
```

Output:

```text
90
```

---

# ➕ 17. sum()

`sum()` calculates the total of numeric values.

```python
marks = {
    "Aman": 75,
    "Rahul": 90,
    "Priyanshu": 85
}

total = sum(marks.values())

print(total)
```

Output:

```text
250
```

---

# 📦 18. Nested Dictionary

A nested dictionary is a dictionary inside another dictionary.

```python
students = {
    "student1": {
        "name": "Priyanshu",
        "marks": 85
    },
    "student2": {
        "name": "Aman",
        "marks": 90
    }
}

print(students["student1"]["name"])
```

Output:

```text
Priyanshu
```

---

# 📋 19. Dictionary with Lists

A dictionary can also store lists as values.

```python
students = {
    "Priyanshu": [85, 90, 88],
    "Aman": [75, 80, 82]
}

print(students["Priyanshu"])
```

Output:

```text
[85, 90, 88]
```

---

# 🔤 20. Character Frequency using Dictionary

A dictionary can be used to count how many times each character appears.

```python
text = "hello"

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print(frequency)
```

Output:

```text
{'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

---

# 💻 Practice Questions

## 🟢 Easy (1–5)

1. Create a dictionary containing your name, age and course.
2. Access and print a particular value.
3. Add a new key-value pair.
4. Update an existing value.
5. Delete a key-value pair.

---

## 🟡 Medium (6–10)

6. Print all keys using `keys()`.
7. Print all values using `values()`.
8. Print key and value together using `items()`.
9. Check whether a particular key exists.
10. Count the number of items in a dictionary.

---

## 🔴 Challenge (11–15)

11. Store 5 students and their marks in a dictionary.
12. Find the student with the highest marks.
13. Calculate the average marks.
14. Count the frequency of each character in a string using a dictionary.
15. Create a nested dictionary containing multiple students.

---

# 🚀 Mini Project — Student Record Management System

Create a menu-driven program for managing student records.

### Menu:

```text
===== STUDENT RECORD SYSTEM =====

1. Add Student
2. View Student
3. Update Marks
4. Delete Student
5. Exit

Enter Choice:
```

### Features:

* Add student record
* View student record
* Update marks
* Delete student record
* Exit program
* Use dictionary to store records
* Use `while` loop for the menu
* Use `if-elif-else` for choices

### Concepts Used:

* Dictionary
* Key-Value pairs
* `get()`
* `pop()`
* `del`
* `in`
* `items()`
* `len()`
* `while` loop
* `if-elif-else`
* User Input

---

# 🛠️ Tools Used

* Python
* VS Code
* Git & GitHub

---

# 👨‍💻 Author

**Priyanshu**
