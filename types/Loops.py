student_names = ["Mark", "John", "Marry"]
for student in student_names:
    print(f"Student name is {student}")

x = 0
for index in range(10):
    x += 10
    print("The value of X is {0}".format(x))

student_names.append("Joshoa")
student_names.append("Tonny")
student_names.append("Alex")
student_names.append("Lora")
student_names.append("Marya")
student_names.append("Ivan")

skipped_name = "Tonny"
searched_name = "Alex"
for name in student_names:
    if name == skipped_name:
        print("Skipping " + skipped_name)
        continue
    if name == searched_name:
        print("We found Him. It is " + name)
        break
    print("Current processed name is {0}".format(name))

x = 0
while x < 10:
    print(f"Count is {x}")
    x += 1
    if x == 7:
        break
