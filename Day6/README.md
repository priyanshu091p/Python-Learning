# 📅 Day 6 – Python Lists 🐍

## 📚 Topics Covered

* What is a List?
* Creating a List
* List Indexing
* Negative Indexing
* List Slicing
* Changing List Elements
* `len()`
* `append()`
* `insert()`
* `remove()`
* `pop()`
* `sort()`
* `reverse()`
* `clear()`

---

# 📋 What is a List?

A list is a collection of multiple values stored in a single variable.

Lists are:

* Ordered
* Changeable
* Allow duplicate values

Example:

```python
marks = [75, 82, 90, 68, 88]

print(marks)
```

Output:

```text
[75, 82, 90, 68, 88]
```

---

# 📝 Creating a List

A list is created using square brackets `[]`.

```python
numbers = [10, 20, 30, 40, 50]

names = ["Priyanshu", "Rahul", "Aman"]
```

---

# 🔢 List Indexing

List indexing is used to access individual elements.

Indexing starts from `0`.

```python
marks = [75, 82, 90, 68, 88]

print(marks[0])
print(marks[2])
```

Output:

```text
75
90
```

---

# 🔙 Negative Indexing

Negative indexing accesses elements from the end of the list.

```python
marks = [75, 82, 90, 68, 88]

print(marks[-1])
print(marks[-2])
```

Output:

```text
88
68
```

---

# ✂️ List Slicing

Slicing is used to get a part of a list.

### Syntax:

```python
list[start:stop]
```

Example:

```python
marks = [75, 82, 90, 68, 88]

print(marks[0:3])
```

Output:

```text
[75, 82, 90]
```

---

# 🔄 Changing List Elements

List elements can be changed because lists are mutable.

```python
marks = [75, 82, 90]

marks[1] = 85

print(marks)
```

Output:

```text
[75, 85, 90]
```

---

# 📏 len()

`len()` returns the number of elements in a list.

```python
numbers = [10, 20, 30, 40]

print(len(numbers))
```

Output:

```text
4
```

---

# ➕ append()

`append()` adds an element to the end of a list.

```python
marks = [75, 82, 90]

marks.append(95)

print(marks)
```

Output:

```text
[75, 82, 90, 95]
```

---

# 📍 insert()

`insert()` adds an element at a specific position.

### Syntax:

```python
list.insert(index, value)
```

Example:

```python
marks = [75, 82, 90]

marks.insert(1, 80)

print(marks)
```

Output:

```text
[75, 80, 82, 90]
```

---

# ❌ remove()

`remove()` removes a specific value from the list.

```python
marks = [75, 82, 90, 68]

marks.remove(68)

print(marks)
```

Output:

```text
[75, 82, 90]
```

---

# 🗑️ pop()

`pop()` removes an element using its index.

```python
marks = [75, 82, 90, 68]

marks.pop(2)

print(marks)
```

Output:

```text
[75, 82, 68]
```

If no index is given, `pop()` removes the last element.

```python
marks.pop()
```

---

# 🔢 sort()

`sort()` arranges list elements in ascending order.

```python
numbers = [50, 20, 40, 10, 30]

numbers.sort()

print(numbers)
```

Output:

```text
[10, 20, 30, 40, 50]
```

---

# 🔄 reverse()

`reverse()` reverses the order of elements.

```python
numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)
```

Output:

```text
[40, 30, 20, 10]
```

---

# 🧹 clear()

`clear()` removes all elements from a list.

```python
numbers = [10, 20, 30]

numbers.clear()

print(numbers)
```

Output:

```text
[]
```

---

# 💻 Practice Questions

## 🟢 Easy (1–5)

1. Create a list of 5 numbers and print it.
2. Print the first and last element.
3. Find the length of a list.
4. Add an element using `append()`.
5. Remove an element using `remove()`.

---

## 🟡 Medium (6–10)

6. Insert an element at a specific position.
7. Print the first 3 elements using slicing.
8. Print the list in reverse.
9. Find the largest and smallest element.
10. Calculate the sum of all elements.

---

## 🔴 Challenge (11–15)

11. Find the second-largest number.
12. Count how many times a particular number occurs.
13. Remove duplicate elements from a list.
14. Separate even and odd numbers into two lists.
15. Find the average of all numbers in a list.

---

# 🚀 Mini Project

## Student Marks Analyzer

Create a program that takes marks of students and analyzes their results using a list.

### Input:

```text
Enter marks: 78 85 92 67 88
```

### Output:

```text
Marks: [78, 85, 92, 67, 88]

Highest Marks: 92
Lowest Marks: 67
Total Marks: 410
Average Marks: 82.0

Passed Subjects: 5
Failed Subjects: 0
```

### ⭐ Extra

Also display:

* Highest marks
* Lowest marks
* Total marks
* Average marks
* Passed subjects
* Failed subjects

---

# 🛠️ Tools Used

* Python
* VS Code
* Git & GitHub

---

# 👨‍💻 Author

**Priyanshu**
