# school adminstration portal
 
 
students_records = []
 
# no arguments here
def register_sudent():
    student_name = input("enter the name:")
    parent_name = input("parent name:")
    student_age = int(input("enter the student age:"))
 
    stu_dict = {
        "student_name":student_name,
        "parent_name":parent_name,
        "student_age":student_age
    }
 
    students_records.append(stu_dict)
    print("student record registerd")
 
    print("*"*20)
 
def view_registered_student():
    print("*"*20)
    print("view students")
    print("*"*20)
 
 
    if len(students_records)==0:
        print("No students registered yet.")
        return
    for index,stu_rec in enumerate(students_records,1):
        print("Student details")
        print("*"*20)
 
        print("student_name:",stu_rec["student_name"])
        print("parent_name:",stu_rec["parent_name"])
        print("student_age:",stu_rec["student_age"])
 
        print("*"*20)
 
 
while True:
 
        print("\n")
        print("1. register student")
        print("2. view details")
        print("3. Exit")
        print("*"*20)
 
        choice = int(input(" Enter your choice:"))
 
        if choice == 1:
            register_sudent()
        elif choice == 2:
            view_registered_student()
        elif choice == 3:
            break
        else:
            print("invalid choice")
            break
 
       
       
 
 
 