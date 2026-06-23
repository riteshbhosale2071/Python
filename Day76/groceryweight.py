def grocery():
    n = int(input("Enter numer of items : "))

    weight = []
    total = 0

    for i in range(n):
        items = float(input(f"Enter weight of item {i+1} (kg) : "))
        weight.append(items)

    for i in weight:
        total += i

    print("Total weight is",total)

grocery()