from pathlib import Path

# Define a relative path to your file
file_path = Path("FOSD")/"uniapp"/"data"/"students.json"

# Get the absolute path (optional)
absolute_path = file_path.resolve()

print(Path("FOSD"))
print(file_path)       # data/students.json (cross-platform)
print(absolute_path)   # Full path on your OS
print(type(file_path))
print(file_path.suffix)

# from pathlib import Path

# # Get the folder of the current script
# base_dir = Path(__file__).parent

# # Then build the path to the target file
# file_path = base_dir / "data" / "files" / "students.json"

# print(base_dir)
# print(file_path)



# How to query and update only specific records in json file
# import json

# # Load data from file
# with open('student_test.json', 'r') as f:
#     students = json.load(f)

# # 🔍 Query: Find student with id == 3
# student = next((s for s in students if s['id'] == 3), None)

# print(student)
# # 🛠 Update: Change only the 'grade' field
# if student:
#     student['grade'] = 'B+'

# # Save changes back to the file
# with open('student_test.json', 'w') as f:
#     json.dump(students, f, indent=4)

# print("Updated student:", student)

# Pretty printing json data
#----------------------------------------------
# import json

# # Load data from file
# with open('student_test.json', 'r') as f:
#     students = json.load(f)
# data = {
#         "id": 3,
#         "name": "Charlie",
#         "age": 23,
#         "grade": "B+"
#     }
# # Save changes back to the file
# with open('student_test.json', 'a') as f:
#     json.dump(data, f, indent=5)



# import json
# from pathlib import Path

# class StudentManager:
#     def __init__(self, filepath):
#         self.filepath = Path(filepath)
#         self.data = self._load_data()

#     def _load_data(self):
#         if self.filepath.exists():
#             with open(self.filepath, 'r') as f:
#                 return json.load(f)
#         return {"students": [], "enrollment": [], "admin": {}}

#     def _save_students(self):
#         # only rewrite students part
#         with open(self.filepath, 'r+') as f:
#             full_data = json.load(f)
#             full_data["students"] = self.data["students"]
#             f.seek(0)
#             json.dump(full_data, f, indent=4)
#             f.truncate()

#     def create_student(self, student):
#         self.data["students"].append(student)
#         self._save_students()
        

#     def delete_student(self, student_id):
#         self.data["students"] = [s for s in self.data["students"] if s["id"] != student_id]
#         self._save_students()

#     def update_student(self, student_id, updates):
#         for student in self.data["students"]:
#             if student["id"] == student_id:
#                 student.update(updates)
#                 break
#         self._save_students()

#     def get_student(self, student_id):
#         return next((s for s in self.data["students"] if s["id"] == student_id), None)



# manager = StudentManager("student_test.json")


# print(manager._load_data())
# print(manager.filepath)
# # Create
# manager.create_student({
#     "id": "3", "name": "Clara", "email": "clara@example.com", "password": "abcd"
# })

# # Read
# print(manager.get_student("3"))

# # # Update
# manager.update_student("3", {"name": "Clara Smith"})

# # Delete
# manager.delete_student("3")
