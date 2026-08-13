# Find duplicate values from a list using a set.
num=[10, 20, 30, 40, 10, 10, 20]
seen=set()
duplicates=set()

for i in num:
    if i in seen:
        duplicates.add(i)
    else:
        seen.add(i)

print("Duplicates value:",duplicates)

# Find common elements between two lists.
num_1=[10, 20, 30, 40, 50]
num_2=[10, 50, 60, 70, 20]
set_1=set(num_1)
set_2=set(num_2)
result=set_1.intersection(set_2)
print(result)


# Find elements present in one list but not another.
num_1=[10, 20, 30, 40, 50]
num_2=[60, 70, 80, 90, 100]
set_1=set(num_1)
set_2=set(num_2)
print(set_1.isdisjoint(set_2))


# Remove duplicates from a list while keeping unique values.
num_1=[10, 20, 30, 40, 50, 10, 20, 30, 30]

unique=[]
for i in num_1:
   if i not in unique:
      unique.append(i)
print(unique)

# Check whether two sets are equal
set_1={10, 20, 30, 40}
set_2={40, 10, 30, 20}

if(set_1==set_2):
    print("Both sets are equal")
else:
    print("Sets are not equal")
