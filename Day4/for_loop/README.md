# Python Learning - Day 4 🐍

## 📌 Topic

Loops in Python (for Loop)

---

# 📚 Topics Covered

* What is a Loop?
* `for` loop syntax
* `range()` function
* `range(start, stop)`
* `range(start, stop, step)`
* Nested `for` loop (Basic)

---

# 🔁 What is a Loop?

A loop is used to execute a block of code repeatedly.

Loops help us:

* Reduce code repetition
* Save time
* Perform repetitive tasks easily

Example:

Without loop:

```python id="4krx7m"
print("Python")
print("Python")
print("Python")
```

Using loop:

```python id="jd8o2a"
for i in range(3):
    print("Python")
```

---

# 🔄 for Loop in Python

A `for` loop is used to iterate over a sequence and execute code multiple times.

## Syntax:

```python id="s7o7g5"
for variable in sequence:
    statement
```

Example:

```python id="9wzq7u"
for i in range(5):
    print(i)
```

Output:

```id="s4khc2"
0
1
2
3
4
```

---

# 🔢 range() Function

The `range()` function generates a sequence of numbers.

---

## 1. range(stop)

Starts from 0 and stops before the given value.

Example:

```python id="c4n3dd"
for i in range(5):
    print(i)
```

Output:

```id="4s4q8f"
0
1
2
3
4
```

---

## 2. range(start, stop)

Starts from the start value and stops before the stop value.

Example:

```python id="d5y8rx"
for i in range(2, 6):
    print(i)
```

Output:

```id="1dq7cb"
2
3
4
5
```

---

## 3. range(start, stop, step)

The step value controls the increment or decrement.

Example:

```python id="2i4s5y"
for i in range(1, 10, 2):
    print(i)
```

Output:

```id="lq5s6p"
1
3
5
7
9
```

---

# 🔁 Nested for Loop

A loop inside another loop is called a nested loop.

Example:

```python id="l0d3up"
for i in range(3):
    for j in range(3):
        print("*")
```

Nested loops are mainly used for:

* Patterns
* Tables
* Matrix operations

---

# 💻 Practice Questions

## 🟢 Easy (1-5)

1. Print numbers from 1 to 10.

2. Print numbers from 10 to 1.

3. Print even numbers from 1 to 100.

4. Print odd numbers from 1 to 100.

5. Print multiplication table of a number.

---

## 🟡 Medium (6-10)

6. Find the sum of first n natural numbers.

7. Find the factorial of a number.

8. Count digits in a number.

9. Reverse a number.

10. Find the sum of digits of a number.

---

## 🔥 Challenge (11-15)

11. Print the pattern:

```
*
**
***
****
*****
```

12. Print the pattern:

```
*****
****
***
**
*
```

13. Print multiplication tables from 1 to 10.

14. Check whether a number is prime.

15. Print Fibonacci series up to n terms.

---

# 🚀 Mini Project

# Number Guessing Game (Without Random)

## Features:

* User enters a guessing number
* Program checks the guess
* Display whether the number is correct or not
* Use loops for repeated attempts

---

## Concepts Used:

* Variables
* Input
* Type Casting
* for Loop
* range()
* Conditional Statements

---

# 🛠️ Tools Used

* Python
* VS Code
* Git & GitHub

---

# 👨‍💻 Author

**Priyanshu**

BCA Student
