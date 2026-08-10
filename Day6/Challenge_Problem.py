#Find the second-largest number.
numbers=[50,40,30,10,20]
numbers.sort()
print("Second largest:",numbers[-2])

#Count how many times a number occurs.
numbers=[50,40,30,10,20,40,50,40,10]
print("40 occurs:",numbers.count(40))
print(numbers.count(50))
print(numbers.count(20))

#Remove duplicate elements from a list.
numbers=[50,40,30,10,20,40,50,40,10]
numbers=list(set(numbers))              #first converts into set and than list 
print(numbers)                          #because set did't contains duplicates values

#Separate even and odd numbers into two lists.
numbers=[1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]

for i in numbers:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)

print("Even:",even)
print("Odd:",odd)

#Find the average of all numbers.
numbers=[10,20,30,40,50]
total=0

for i in numbers:
    total=total+i

average=total/len(numbers)
print("Average:",average)