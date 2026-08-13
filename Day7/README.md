📅 Day 7 — Python Tuples & Sets 🐍
📚 Part 1 — Tuples
Topics Covered
What is a Tuple?
Creating a Tuple
Tuple Indexing
Negative Indexing
Tuple Slicing
Tuple is Immutable
len()
count()
index()
List vs Tuple
📦 1. What is a Tuple?

A tuple is a collection used to store multiple values.

Tuples are ordered and immutable, which means their elements cannot be changed after creation.

Example:

numbers = (10, 20, 30, 40, 50)

print(numbers)

Output:

(10, 20, 30, 40, 50)
📝 2. Creating a Tuple

Tuples are usually created using parentheses ().

numbers = (10, 20, 30, 40)

names = ("Priyanshu", "Sumit", "Ayan")

A single-element tuple needs a comma:

number = (10,)
🔢 3. Tuple Indexing

Tuple indexing works like list indexing.

Indexing starts from 0.

numbers = (10, 20, 30, 40)

print(numbers[0])
print(numbers[2])

Output:

10
30
🔙 4. Negative Indexing

Negative indexing accesses elements from the end.

numbers = (10, 20, 30, 40)

print(numbers[-1])
print(numbers[-2])

Output:

40
30
✂️ 5. Tuple Slicing

Slicing is used to get a part of a tuple.

numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])

Output:

(20, 30, 40)
🔒 6. Tuple is Immutable

Immutable means that tuple elements cannot be changed after creation.

numbers = (10, 20, 30)

# numbers[0] = 100  ❌

This will produce an error because tuples cannot be modified.

📏 7. len()

len() returns the number of elements in a tuple.

numbers = (10, 20, 30, 40)

print(len(numbers))

Output:

4
🔢 8. count()

count() tells how many times a value appears in a tuple.

numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))

Output:

3
🔍 9. index()

index() returns the position of the first occurrence of a value.

numbers = (10, 20, 30, 40)

print(numbers.index(30))

Output:

2
⚖️ 10. List vs Tuple
List	Tuple
Uses []	Uses ()
Mutable	Immutable
Elements can be changed	Elements cannot be changed
More suitable for changing data	More suitable for fixed data
💻 Tuple Practice
Create a tuple of 5 numbers.
Print the first and last element.
Find its length.
Count how many times a number occurs.
Find the index of a particular element.
📚 Part 2 — Sets
Topics Covered
What is a Set?
Creating a Set
Duplicate Values
add()
remove()
discard()
pop()
union()
intersection()
difference()
Removing Duplicates Using Sets
Finding Common Elements
Finding Unique Elements
Comparing Sets
📦 1. What is a Set?

A set is a collection of unique values.

Sets do not allow duplicate values.

Example:

numbers = {10, 20, 30, 40}

print(numbers)
📝 2. Creating a Set

Sets are created using curly brackets {}.

numbers = {10, 20, 30, 40}

An empty set is created using:

numbers = set()
🚫 3. Duplicate Values

Duplicate values are automatically removed from a set.

numbers = {10, 20, 20, 30, 30}

print(numbers)

Output:

{10, 20, 30}
➕ 4. add()

add() adds a new element to a set.

numbers = {10, 20, 30}

numbers.add(40)

print(numbers)
❌ 5. remove()

remove() removes a specific element.

numbers = {10, 20, 30}

numbers.remove(20)

print(numbers)

If the element does not exist, remove() raises an error.

🗑️ 6. discard()

discard() also removes an element.

The difference is that discard() does not raise an error if the element is missing.

numbers = {10, 20, 30}

numbers.discard(50)

print(numbers)
🎲 7. pop()

pop() removes and returns an arbitrary element from a set.

numbers = {10, 20, 30}

numbers.pop()

print(numbers)
🔗 8. union()

union() combines the elements of two sets.

set1 = {10, 20, 30}
set2 = {30, 40, 50}

print(set1.union(set2))

Result:

{10, 20, 30, 40, 50}
🤝 9. intersection()

intersection() returns the elements that are common in both sets.

set1 = {10, 20, 30}
set2 = {20, 30, 40}

print(set1.intersection(set2))

Result:

{20, 30}
➖ 10. difference()

difference() returns elements that are present in one set but not the other.

set1 = {10, 20, 30}
set2 = {20, 30, 40}

print(set1.difference(set2))

Result:

{10}
💻 Set Practice
Create a set with duplicate values and observe the output.
Add a new element.
Remove an element.
Find union of two sets.
Find intersection of two sets.
🔥 Challenge Questions
Find duplicate values from a list using a set.
Find common elements between two lists.
Find elements present in one list but not another.
Remove duplicates from a list while keeping unique values.
Check whether two sets are equal.
🚀 Mini Project
Duplicate & Common Element Finder

Create a program that compares two lists using sets.

Input:
List 1: [10, 20, 30, 20, 40, 50]
List 2: [20, 30, 60, 70, 30]
Output:
Unique List 1: {10, 20, 30, 40, 50}
Unique List 2: {20, 30, 60, 70}

Common Elements: {20, 30}

Only in List 1: {10, 40, 50}
Only in List 2: {60, 70}
Concepts Used:
Lists
Sets
Removing duplicates
set()
union()
intersection()
difference()
User Input
Set comparison
🛠️ Tools Used
Python
VS Code
Git & GitHub
👨‍💻 Author

Priyanshu