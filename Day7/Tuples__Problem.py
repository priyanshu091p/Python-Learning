# Create a tuple of 5 numbers.
tuple=(1,"Priyanshu",23,34.4,(1,2,3,4))
print(tuple)

# Print first and last element.
tuple=(1,"Priyanshu",23,34.4,(1,2,3,4))
print(tuple[0])
print(tuple[-1])

# Find its length.
print(len(tuple))

# Count how many times a number occurs.
tuple=(1,"Priyanshu",23,34.4,(1,2,3,4),1,1)
print("Number of repeated 1 is:",tuple.count(1))


# Find the index of a particular element.
tuple=(1,"Priyanshu",23,34.4,(1,2,3,4))
print(tuple.index(1))
print(tuple.index("Priyanshu"))
print(tuple.index(23))
print(tuple.index(34.4))
print(tuple.index((1,2,3,4)))