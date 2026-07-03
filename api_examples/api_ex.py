#need to install fastapi uvicorn
#pip install fastapi uvicorn
#running command uvicorn api_ex:fastapi_obj --reload
from fastapi import FastAPI
import uvicorn
from yasvanth_school import yasvanth_school
from yasvanth_school import tenth_class ,eleventh_class,twelth_class,driving


fastapi_obj=FastAPI(title="sample api's")

@fastapi_obj.get("/hello_world")
def welcome():
    return "hello world is running"

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

#tenth calss winner

@fastapi_obj.post("/tenth_winner")
def tenth_winner(std:str,sports_winner:str,sec:str):
    tenth_class_obj=tenth_class(std,sports_winner,sec)
    return {
        "details":tenth_class_obj.sports_winner()
    }

@fastapi_obj.post("/eligible_or_not")
def eligibility(person_age:int,person_name:str):
    driving_obj=driving(age=person_age,name=person_name)
    return {
        "status":driving_obj.eligible_or_not(),
        "total count":driving_obj.count_eligible()
    }
    
    