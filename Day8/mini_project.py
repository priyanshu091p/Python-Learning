# Mini Project — Student Record Management System
'''===== STUDENT RECORD SYSTEM =====

1. Add Student
2. View Student
3. Update Age
4. Delete Student
5. Exit

Enter Choice:'''

students = {                        #Dictionary create
    "s_1":{
        "name"  : "Priyanshu",
        "age"   : 21,
        "city"  : "ghaziabad"
    },
    "s_2":{
        "name"  : "Sumit",
        "age"   : 19,
        "city"  : "ghaziabad"
    }
}

print("=====STUDENT RECORD SYSTEM=====")        #Menu
print("1. Add Student")
print("2. View Student")
print("3. Update Marks")
print("4. Delete Student")
print("5. Exit")


while(True):
    choice = input("Enter your choice: ")

    if(choice=="1"):
        
        student_id = input("Enter student ID: ")

        if(student_id in students):
            print("Student ID already exists!")
        else:
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            city= input("Enter student city: ")

            students[student_id] ={
                "name"  : name,
                "age"   : age,
                "city"  : city
            }
            print("Student added successfully!")

    elif(choice=="2"):

        student_id = input("Enter student ID: ")

        if(student_id in students):
            print("===Student Details===")
            print("Name:", students[student_id]["name"])
            print("Age:", students[student_id]["age"])
            print("City:", students[student_id]["city"])
        else:
            print("student not found")

    elif(choice=="3"):

        student_id = input("Enter student ID: ")

        if(student_id in students):
            updated_age = int(input("Enter new age of student: "))
            students[student_id]["age"] = updated_age
            
            print("Age Update")
        else:
            print("Student not found")

    elif(choice=="4"):

        student_id = input("Enter student ID: ")

        if(student_id in students):
            del students[student_id]
            print("Student delete successfully! ")
        else:
            print("Student not found")

    elif(choice=="5"):

        print("Thank you")
        break

    else:
        print("Invalid choice!")
    

    

        

    



        



