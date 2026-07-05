import json

class StudentService:
    def __init__(self):
        self.file_name="students.json"
  # get all student  
    def get_all_student(self):
        with open(self.file_name, "r") as file:

            return json.load(file)
    
# new student registration
    
    def add_student(self, student):
        students = self.get_all_student()
        # Validation
        for s in students:
            if s["student id"] == student["student id"]:
                return {"message": "Student ID already exists"}
        students.append(student)
        with open(self.file_name, "w") as file:
            json.dump(students, file, indent=4)
        return {"message": "Student Added Successfully"}