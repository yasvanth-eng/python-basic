# Fist we need to install uvicorn and fastapi ( pip install uvicorn fastapi)
# running command - uvicorn (file name):app --reload
 
# Get all students
# New student registeration
# Get student by id
# Update student by id
# Delete student by id

 
from fastapi import FastAPI, HTTPException
from students_service_class import StudentService
import json
from fastapi.middleware.cors import CORSMiddleware
 
app = FastAPI(title="Student CRUD API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

stu_obj=StudentService()

login_info = "./login_details.json"

@app.get("/health_check")
def health_check():
    try:
        return {"message": "API is running"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Application failed: {str(e)}")

#get all student api

@app.get("/students")
def students():
    try:
        total_student=stu_obj.get_all_student()
        print(total_student)
        if len(total_student)==0:
            return []
           
        else:
           return total_student
        
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Application failed: {str(e)}")


#new student api

@app.post("/students")
def new_student_registration(student_id:int,student_name:str,age:int,student_class:int):
    #try:
        new_student_details={
        "student_id":student_id,
        "student_name":student_name,
        "age":age,
        "student_class":student_class

    }
        print("new student details",new_student_details)
        return stu_obj.add_student(new_student_details)
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=f"Application failed: {str(e)}")

# find student by student_id

@app.get("/students/{student_id}")
def get_student(student_id:int):
    try:
        stu_record=stu_obj.get_student_by_id(student_id)
        return stu_record
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Application failed: {str(e)}")


@app.delete("/students/{student_id}")
def delete_student(student_id:int):
    try:
        deleted_record=stu_obj.delete_by_id(student_id)
        return deleted_record
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Application failed: {str(e)}")


@app.put("/students/{student_id}") 
def update_stu_details(student_id:int,student_name:str,age:int,student_class:int):
    try:
        updated_stu=stu_obj.update_student_record(student_id,student_name,age,student_class)
        return updated_stu
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Application failed: {str(e)}")
    

@app.post("/admin/login")
def admin_login(username:str,password:str):
    
    with open(login_info, "r") as f:
        login_details = json.load(f)
    if username == login_details["admin"]["username"] and password == login_details["admin"]["password"]:
        return {"message": "Login successful"}
    else:
        return {"message": "Invalid username or password"}


@app.post("/student/student_login_register")
def student_login_register(username: str, password: str,re_enter_password: str):
    with open(login_info, "r") as f:
        login_details = json.load(f)
 
    # Check if the student already exists
    for student in login_details["student_login"]:
        if student["username"] == username:
            return {"message": "Student already registered"}
    if password != re_enter_password:
        return {"message": "Passwords do not match"}
    # Register the new student
    login_details["student_login"].append({"username": username, "password": password})
    with open(login_info, "w") as f:
        json.dump(login_details, f,indent=4)
 
    return {"message": "Student registered successfully"}
 
@app.post("/student/login")
def student_login(username: str, password: str):
    with open(login_info, "r") as f:
        login_details = json.load(f)
    for student in login_details["student_login"]:
        if student["username"] == username and student["password"] == password:
            return {"message": "Login successful"}
    return {"message": "Invalid username or password"}
 