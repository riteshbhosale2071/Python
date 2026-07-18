def equaldistribution():
    total_amount = int(input("Enter total amount (in crores): "))
    people = int(input("Enter number of people: "))

    if people == 0:
        print("Division by zero is not allowed.")
        return

    amount_per_person = total_amount / people

    print("Amount each person gets =", amount_per_person, "crores")

equaldistribution()