#Insert an element at a specific position.
list=[2,4,5,3,7]
list.insert(2,8)
print(list)

#Print the first 3 elements using slicing.
list=[2,4,5,3,7]
print(list[0:3])

#Reverse a list.
list=[2,4,5,3,7]
list.reverse()
print(list)

#Find the largest and smallest number.
list=[2,4,5,3,7]
print("Largest:",max(list))
print("smallest:",min(list))

#Find the sum of all elements.
list=[1,2,3,4,5]

'''sum=0
for i in list:
    sum+=i
print(f"Sum : {sum}")''' 

print("Sum:",sum(list))
    
