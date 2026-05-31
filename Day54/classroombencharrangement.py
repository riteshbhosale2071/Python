def find():
    students = int(input("Enter total students: "))
    
    bench_capacity = int(input("Students per bench: "))

    benches = students // bench_capacity

    if students % bench_capacity != 0:
        benches += 1

    print("Total Benches Required =", benches)

find()