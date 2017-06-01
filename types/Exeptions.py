student = {
    "name": "Mark",
    "id": 124,
    "feedback": None
}

try:
    last_name = student["last_name"]
    print(last_name)
except KeyError:
    print("Error finding last_name")
except TypeError as error:
    print(error)

print("EXECUTE")
