#Create a dictionary containing your name, age and course.
student = {
    "name"  : "Priyanshu",
    "age"   : 21,
    "course": "BCA"
}

print(student)

# Access and print a particular value.
student = {
    "name"  : "Priyanshu",
    "age"   : 21,
    "course": "BCA"
}

print(student["name"])
print(student["age"])
print(student["course"])

# Add a new key-value pair.
student = {
    "name"  : "Priyanshu",
    "age"   : 21,
    "course": "BCA"
}

student["city"] = "Ghaziabad"
print(student)

# Update an existing value.
student = {
    "name"  : "Priyanshu",
    "age"   : 21,
    "course": "BCA"
}

student["age"] = 22
print(student["age"])

# Delete a key-value pair.
student = {
    "name"  : "Priyanshu",
    "age"   : 21,
    "course": "BCA"
}

del student["age"]
print(student)