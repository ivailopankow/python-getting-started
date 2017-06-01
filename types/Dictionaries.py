student = {
    "name": "Mark",
    "id": 124,
    "feedback": None
}
print(student)

all_students =[
    {"name": "Mark", "id": 12},
    {"name": "Penka", "id": 13}
]
for student in all_students:
    print(student["name"])
    print(student.get("lastName", "Unknown"))
    print(student.keys())
    print(student.values())

all_students[0]["name"] = "James"
print(all_students[0])
del all_students[0]["name"]
print(all_students)
