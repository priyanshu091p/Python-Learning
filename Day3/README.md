# Python Learning - Day 3 🐍

## 📌 Topic

Conditional Statements in Python

---

# 📚 Theory Topics Covered

* `if` statement
* `if-else` statement
* `if-elif-else` statement
* Nested `if`
* Indentation in Python

---

# 🔀 Conditional Statements

Conditional statements are used to make decisions in a program.

They execute different blocks of code based on conditions.

---

# 1. if Statement

The `if` statement executes code only when the condition is True.

### Syntax:

```python
if condition:
    statement
```

Example:

```python
age = 18

if age >= 18:
    print("Eligible to vote")
```

---

# 2. if-else Statement

The `if-else` statement executes one block when the condition is True and another block when it is False.

### Syntax:

```python
if condition:
    statement
else:
    statement
```

Example:

```python
number = 5

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

# 3. if-elif-else Statement

Used when we have multiple conditions.

### Syntax:

```python
if condition1:
    statement
elif condition2:
    statement
else:
    statement
```

Example:

```python
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
else:
    print("Grade C")
```

---

# 4. Nested if

A condition inside another condition is called nested if.

Example:

```python
age = 20

if age >= 18:
    if age <= 60:
        print("Eligible")
```

---

# 📏 Indentation in Python

Indentation means spaces at the beginning of a line.

Python uses indentation to define blocks of code.

Correct:

```python
if True:
    print("Hello")
```

Incorrect:

```python
if True:
print("Hello")
```

---

# 💻 Practice Questions

## 🟢 Easy (1-5)

1. Check whether a number is positive or negative.

2. Check whether a number is even or odd.

3. Find the greater of two numbers.

4. Find the largest of three numbers.

5. Check whether a person is eligible to vote.

---

## 🟡 Medium (6-10)

6. Check whether a year is a leap year.

7. Check whether a character is a vowel or consonant.

8. Check whether a student has passed.

Condition:

```
Marks >= 33
```

9. Find the greatest of four numbers.

10. Check whether a number is divisible by both 5 and 11.

---

## 🔥 Challenge (11-15)

11. Grade Calculator

Grades:

* A
* B
* C
* D
* F

12. Electricity Bill Calculator using slabs.

13. Income Tax Calculator (basic).

14. ATM Withdrawal Check.

Conditions:

* Check account balance
* Check withdrawal amount

15. Login System.

Features:

* Username verification
* Password verification

---

# 🚀 Mini Project

# Student Result Management System

## Features:

* Student Name
* Roll Number
* Marks of 5 Subjects
* Total Marks
* Percentage
* Grade Calculation
* Pass/Fail Status

---

## Concepts Used:

* Variables
* Input
* Type Casting
* Arithmetic Operators
* Conditional Statements
* if-elif-else

---

## Example Output:

```
Student Result

Name: Priyanshu
Roll Number: 101

Total Marks: 425
Percentage: 85%

Grade: A
Status: Pass
```

---

# 🛠️ Tools Used

* Python
* VS Code
* Git & GitHub

---

# 👨‍💻 Author

**Priyanshu**

BCA Student
