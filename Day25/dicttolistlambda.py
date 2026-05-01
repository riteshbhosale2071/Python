students = [
    {"name": "Ritesh", "marks": 85},
    {"name": "Amit", "marks": 70},
    {"name": "Neha", "marks": 90}
]
print(students)
names = list(map(lambda a: a["name"] ,students))
print(names)