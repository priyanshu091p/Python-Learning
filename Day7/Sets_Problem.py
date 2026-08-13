#Create a set with duplicate values and observe the output.
sets={1,2,3,4,4,2}
print(sets)         #duplicates automtically removed 

#Add a new element.
sets.add(5)
print(sets)

#Remove an element.
sets.remove(1)
#sets.remove(6)       #the work of remove and discard is same differance is 
sets.discard(2)       #remove gives error if item not exist and discard gives not
sets.discard(6)
print(sets)

#Find union of two sets.
set_1={10, 20, 30, 40}
set_2={40, 50, 60, 80}
print(set_1.union(set_2))       #unordered

#Find intersection of two sets.
set_1={10, 20, 30, 40}
set_2={40, 50, 60, 80}
print(set_1.intersection(set_2))

#update()
set_1={10, 20, 30, 40}
set_2={40, 50, 60, 80}
set_1.update(set_2)
print(set_1)
