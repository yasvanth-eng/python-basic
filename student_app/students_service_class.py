import json


class StudentService:
    def __init__(self):
        self.file_name = "students.json"

    # get all student
    def get_all_student(self):
        with open(self.file_name, "r") as file:

            return json.load(file)

    # new student registration

    def add_student(self, student):
        students = self.get_all_student()
        # Validation
        for s in students:
            if s["student_id"] == student["student_id"]:
                return {"message": "Student ID already exists"}
        students.append(student)
        with open(self.file_name, "w") as file:
            json.dump(students, file, indent=4)
        return {"message": "Student Added Successfully"}

    def get_student_by_id(self, student_id):
        student = self.get_all_student()
        for s in student:
            if s["student_id"] == student_id:
                return {"student record": s}
        return {"message": "record not found"}

    def delete_by_id(self, student_id):
        student = self.get_all_student()
        for s in student:
            if s["student_id"] == student_id:
                student.remove(s)
                with open(self.file_name, "w") as file:
                    json.dump(student, file, indent=4)
                return {"message": "record got deleted"}
        return {"message": "record not found"}

    def update_student_record(self, student_id, s_name):

        student = self.get_all_student()
        for s in student:
            if s["student_id"] == student_id:
                s["student_name"] == s_name
                print(s)
                with open(self.file_name, "w") as file:
                    json.dump(student, file, indent=4)
                return {"message": "record got updated sucessfully"}
        return {"message": "record not found"}
