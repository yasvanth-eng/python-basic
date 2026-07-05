# Fist we need to install uvicorn and fastapi ( pip install uvicorn fastapi)
# running command - uvicorn (file name):app --reload
 
# Get all students
# New student registeration
# Get student by id
# Update student by id
# Delete student by id

 
from fastapi import FastAPI, HTTPException
from students_service_class import StudentService
 
app = FastAPI(title="Student CRUD API")

stu_obj=StudentService()

@app.get("/health_check")
def health_check():
    try:
        return {"message": "API is running"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Application failed: {str(e)}")

#get all student api

@app.get("/get_all_students")
def students():
    try:
        total_student=stu_obj.get_all_student()
        if len(total_student)==0:
            return {
                "messages":"no student registered yet"
            }
        else:
            return {
                "messages":total_student
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Application failed: {str(e)}")


#new student api

@app.post("/new_student_registration")
def new_student_registration(id:int,s_name,s_age,s_class):
    new_student_details={
        "student id":id,
        "student name":s_name,
        "student age":s_age,
        "student class":s_class

    }

    return stu_obj.add_student(new_student_details)


    