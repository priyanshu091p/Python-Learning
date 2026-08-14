#Print all keys using keys().
student = {
    "name"  : "Priyanshu",
    "age"   : 21,
    "course": "BCA"
}

print(student.keys())

# Print all values using values().
student = {
    "name"  : "Priyanshu",
    "age"   : 21,
    "course": "BCA"
}

print(student.values())

# Print key and value together using items().
student = {
    "name"  : "Priyanshu",
    "age"   : 21,
    "course": "BCA"
}

print(student.items())

# Check whether a particular key exists.
student = {
    "name"  : "Priyanshu",
    "age"   : 21,
    "course": "BCA"
}

print("name" in student)

# Count the number of items in a dictionary.
student = {
    "name"  : "Priyanshu",
    "age"   : 21,
    "course": "BCA"
}

print(len(student))