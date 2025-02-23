# students = [
#     {"name": "Alice", "score": 90},
#     {"name": "Bob", "score": 85},
#     {"name": "Charlie", "score": 85},
#     {"name": "David", "score": 92}
# ]


# # sorted_students = sorted(students, key=lambda student: (student["score"], student["name"]))

# # print(sorted_students)

# def sort_key(student):
#     return (student["name"], student["score"]) #sort by score first and then by name

# # sorted_students = sorted(students) --------------------......>>>>>>> tries to compare with dictionary object directly which is not supported by python...
# sorted_students = sorted(students, key=sort_key)

# print(sorted_students)

################################################################################################################################################################

employees = [
    {"name": "John", "age": 30, "salary": 50000},
    {"name": "Alice", "age": 25, "salary": 60000},
    {"name": "Bob", "age": 28, "salary": 60000},
    {"name": "Eve", "age": 35, "salary": 45000}
]

# Corrected sorting function (salary descending, age ascending)
def sort_key(employee):
    return (employee["salary"], employee["age"])  # Negative salary for descending order

sorted_employees = sorted(employees, key=sort_key)

print(sorted_employees)
