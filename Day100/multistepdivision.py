def divisionwordproblem():
    total_items = int(input("Enter total items: "))
    groups = int(input("Enter number of groups: "))

    if groups == 0:
        print("Division by zero is not allowed.")
        return

    items_per_group = total_items // groups

    print("\nWord Problem:")
    print("There are", total_items, "books.")
    print("They are divided equally among", groups, "students.")
    print("Each student gets", items_per_group, "books.")

divisionwordproblem()