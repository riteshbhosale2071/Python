students = [("Ritesh", 85), ("Amit", 70), ("Neha", 35), ("Karan", 37)]
print(students)
res = list(filter(lambda a: a[1] > 40 ,students))
print(res)