#need to install fastapi uvicorn
#pip install fastapi uvicorn
from fastapi import FastAPI
import uvicorn
from yasvanth_school import yasvanth_school

fastapi_obj=FastAPI(title="sample api's")

@fastapi_obj.get("/hello_world")
def welcome():
    return "hello world is running"

# if __name__ == "__main__":
#     uvicorn.run()

yasvanth_school_obj=yasvanth_school()
@fastapi_obj.get("/get_all_student_record")
def get_all_student_record():
    return {
        "total student":[
            yasvanth_school_obj.classten(),
            yasvanth_school_obj.classeleven(),
            yasvanth_school_obj.classtwelve(),
        ]
    }