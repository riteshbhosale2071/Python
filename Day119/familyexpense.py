def familyexpense():
    food = float(input("Enter food expense: "))
    rent = float(input("Enter rent expense: "))
    transport = float(input("Enter transport expense: "))
    other = float(input("Enter other expenses: "))

    total = food + rent + transport + other

    print("Total Family Expense:", round(total, 2))

    if food >= rent and food >= transport and food >= other:
        print("Highest Expense: Food")
    elif rent >= food and rent >= transport and rent >= other:
        print("Highest Expense: Rent")
    elif transport >= food and transport >= rent and transport >= other:
        print("Highest Expense: Transport")
    else:
        print("Highest Expense: Other")

familyexpense()