# Python Learning - Day 4 🐍

## 📌 Topic

While Loop in Python

---

# 📚 Topics Covered

* `while` loop
* Infinite loop
* `break`
* `continue`
* `pass`
* Difference between `for` and `while`

---

# 🔄 while Loop in Python

A `while` loop is used to execute a block of code repeatedly as long as a condition is True.

## Syntax:

```python id="0q9b6v"
while condition:
    statement
```

Example:

```python id="f2r7x8"
i = 1

while i <= 5:
    print(i)
    i += 1
```

Output:

```id="1o5t8n"
1
2
3
4
5
```

---

# ♾️ Infinite Loop

An infinite loop is a loop that never stops because the condition always remains True.

Example:

```python id="d3j9bs"
while True:
    print("Hello")
```

To stop an infinite loop, we use `break`.

---

# 🛑 break Statement

`break` is used to immediately stop the loop.

Example:

```python id="4d9k9s"
i = 1

while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1
```

Output:

```id="7i3b1h"
1
2
3
4
```

---

# ⏭️ continue Statement

`continue` skips the current iteration and moves to the next iteration.

Example:

```python id="r0p8o6"
i = 0

while i < 5:
    i += 1

    if i == 3:
        continue

    print(i)
```

Output:

```id="9m6m1e"
1
2
4
5
```

---

# ⏸️ pass Statement

`pass` is used when we want to keep a block empty temporarily.

Example:

```python id="8o8r5t"
while True:
    pass
```

---

# 🔁 Difference Between for and while Loop

| for Loop                                | while Loop                                     |
| --------------------------------------- | ---------------------------------------------- |
| Used when number of iterations is known | Used when condition-based repetition is needed |
| Works with sequences                    | Works with conditions                          |
| Uses range() mostly                     | Requires updating condition manually           |
| Example: printing 1 to 10               | Example: menu-driven programs                  |

---

# 💻 Practice Questions

## 🟢 Easy (1-5)

1. Print numbers from 1 to 10 using while loop.

2. Print numbers from 10 to 1.

3. Print even numbers from 1 to 50.

4. Print odd numbers from 1 to 50.

5. Print multiplication table of a number.

---

## 🟡 Medium (6-10)

6. Find the sum of first n natural numbers.

7. Find the factorial of a number.

8. Reverse a number.

9. Find the sum of digits of a number.

10. Count the digits in a number.

---

## 🔥 Challenge (11-15)

11. Check whether a number is a palindrome.

12. Check whether a number is an Armstrong number.

13. Print Fibonacci series using while loop.

14. Print all prime numbers from 1 to n.

15. Create a menu that keeps running until the user chooses Exit.

---

# 🚀 Mini Project

# ATM System

## Features:

* Check Balance
* Deposit Money
* Withdraw Money
* Exit

---

## Concepts Used:

* `while` loop
* `if-elif-else`
* `break`
* Variables
* User Input

---

## Example:

```
ATM Menu

1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit

Enter your choice:
```

---

# 🛠️ Tools Used

* Python
* VS Code
* Git & GitHub

---

# 👨‍💻 Author

**Priyanshu Singh**

BCA Student
