from itertools import groupby

employees = [
    {"name": "Amit", "dept": "IT"},
    {"name": "Ritesh", "dept": "HR"},
    {"name": "Neha", "dept": "IT"},
    {"name": "Karan", "dept": "HR"},
]

employees.sort(key=lambda x: x["dept"])

grouped = {
    k: list(v)
    for k, v in groupby(employees, key=lambda x: x["dept"])
}
print(grouped)