# Store 5 students and their marks in a dictionary.
students = {
    "Priyanshu" : 85,
    "Sumit"     : 90,
    "Ayan"      : 80,
    "Shivam"    : 75,
    "Vansh"     : 88
}

print(students)

# Find the student with the highest marks.
students = {
    "Priyanshu" : 85,
    "Sumit"     : 90,
    "Ayan"      : 80,
    "Shivam"    : 75,
    "Vansh"     : 77
}

student = max(students, key=students.get)
highest_marks = (max(students.values()))
print("Student:",student)
print("Heighest Marks:",highest_marks)

# Calculate the average marks.
students = {
    "Priyanshu" : 85,
    "Sumit"     : 90,
    "Ayan"      : 80,
    "Shivam"    : 75,
    "Vansh"     : 77
}

average = sum(students.values()) / len(students)
print(f"Average Marks : {average}")

# Count the frequency of each character in a string using a dictionary.
students = "hello"
frequency ={}
for char in students: 
    frequency[char] = frequency.get(char,0) + 1

print(frequency)

# Create a nested dictionary containing multiple students.
students = {
    "s_1": {
        "name"  : "Priyanhsu",
        "age"   : 21,
        "city"  : "Ghaziabad"
    },
    "s_2": {
        "name"  : "Sumit",
        "age"   : 19,
        "city"  : "Ghaziabad"
    },
    "s_3": {
        "name"  : "Ayan",
        "age"   : 19,
        "city"  : "Ghaziabad"
    }
}

print(students["s_1"])
print(students["s_2"])
print(students["s_3"])

print(students["s_1"]["name"])
    