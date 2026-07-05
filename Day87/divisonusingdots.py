def divdots():
    total_dots = int(input("Enter the total number of dots: "))
    groups = int(input("Enter the number of groups: "))

    if groups <= 0:
        print("Number of groups must be greater than 0.")
        return

    dots_per_group = total_dots // groups
    remainder = total_dots % groups

    print("\nDivision Using Dots")
    print("-" * 35)

    for i in range(groups):
        print("Group", i + 1, ":", end=" ")
        for j in range(dots_per_group):
            print("●", end=" ")
        print()

    if remainder > 0:
        print("\nRemaining Dots:", end=" ")
        for i in range(remainder):
            print("●", end=" ")
        print()

    print("\nDots per Group =", dots_per_group)
    print("Remainder =", remainder)

divdots()