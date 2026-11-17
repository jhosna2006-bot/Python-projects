[10:01, 17/11/2026] !: student = {
  "name" : "josh",
  "dept" : "cse",
  "age" : 21,
  "marks" : 95
}

print(student["name"])
print(student.get("age"))
student["city"] = "bangalore"
student["marks"] = 90
print(student["city"])

print(student)

for key, value in student.items():
  print(key,":",value)

print(student.keys())
print(student.values())
[10:01, 17/11/2026] !: contact = ("josh", 21, "student")

name, age, designation = contact

print(name)
print(age)
print(designation)