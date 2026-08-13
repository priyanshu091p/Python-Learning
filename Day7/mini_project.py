#Duplicate & Common Element Finder

'''Input:
List 1: [10, 20, 30, 20, 40, 50]
List 2: [20, 30, 60, 70, 30]

Output:
Unique List 1: {10, 20, 30, 40, 50}
Unique List 2: {20, 30, 60, 70}

Common Elements: {20, 30}
Only in List 1: {10, 40, 50}
Only in List 2: {60, 70}'''

List_1=[10, 20, 30, 20, 40, 50]
List_2=[20, 30, 60, 70, 30]
unique_1=[]
unique_2=[]


for i in List_1:
    if i not in unique_1:
        unique_1.append(i)
for i in List_2:
    if i not in unique_2:
        unique_2.append(i)

common=set(List_1).intersection(set(List_2))
result_1=(set(List_1)) - (set(List_2))
result_2=(set(List_2)) - (set(List_1))

print(unique_1)
print(unique_2)
print("Common Elements:",common)
print("Only in List 1:",result_1)
print("Only in List 2:",result_2)