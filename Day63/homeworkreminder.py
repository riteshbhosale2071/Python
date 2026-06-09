def homework():
    n = int(input("How many homework tasks? "))

    for i in range(n):
        task = input("Enter homework: ")
        print("Reminder:", task)

homework()