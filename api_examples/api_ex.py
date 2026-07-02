#need to install fastapi uvicorn
#pip install fastapi uvicorn
from fastapi import FastAPI
import uvicorn

fastapi_obj=FastAPI(title="sample api's")

@fastapi_obj.get("/hello_world")
def welcome():
    return "hello world is running"

# if __name__ == "__main__":
#     uvicorn.run()

@fastapi_obj.get("addition")