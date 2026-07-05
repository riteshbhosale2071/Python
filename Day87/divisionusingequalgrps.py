def equalgrps():
    total_items = int(input("Enter the total number of items: "))
    groups = int(input("Enter the number of groups: "))

    if groups <= 0:
        print("Number of groups must be greater than 0.")
        return

    items_per_group = total_items // groups
    remainder = total_items % groups

    print("\nDivision Using Equal Groups")
    print("-" * 35)
    print("Total Items      =", total_items)
    print("Number of Groups =", groups)
    print("Items per Group  =", items_per_group)
    print("Remaining Items  =", remainder)

equalgrps()