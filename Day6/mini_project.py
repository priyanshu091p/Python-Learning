#Student Marks Analyzer

'''Input:
Enter marks: 78 85 92 67 88

Output:
Marks: [78, 85, 92, 67, 88]
Highest Marks: 92
Lowest Marks: 67
Total Marks: 410
Average Marks: 82.0

⭐ Bonus
Also show:
Passed Subjects: 5
Failed Subjects: 0'''

marks=list(map(int,input("Enter marks: ").split()))
total=0
passed=0
failed=0

highest=max(marks)
lowest=min(marks)
total=sum(marks)
average=total/len(marks)
for  mark in marks:
    if(mark>=40):
        passed+=1
    else:
        failed+=1

print("Marks:",marks)
print("Higest Marks:",highest)
print("Lowest Marks:",lowest)
print("Total Marks:",total)
print("Average Marks:",average)
print("Passed Subject:",passed)
print("Failed Subject:",failed)