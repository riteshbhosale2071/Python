def setbuilderfromconditions():
    print("Set Builder from Conditions :")

    n = int(input("Enter the number of elements in the universal set: "))

    if n <= 0:
        print("Number of elements must be greater than zero.")
        return

    universal_set = []

    for i in range(n):
        value = int(input("Enter element " + str(i + 1) + ": "))

        if value not in universal_set:
            universal_set.append(value)

    print("\nUniversal Set:", universal_set)

    print("\nChoose a condition:")
    print("1. Even numbers")
    print("2. Odd numbers")
    print("3. Positive numbers")
    print("4. Negative numbers")
    print("5. Numbers greater than a limit")
    print("6. Numbers less than a limit")
    print("7. Numbers divisible by a given number")
    print("8. Numbers within a specified range")

    choice = int(input("Enter your choice (1-8): "))

    result_set = []

    if choice == 1:
        for value in universal_set:
            if value % 2 == 0:
                result_set.append(value)

    elif choice == 2:
        for value in universal_set:
            if value % 2 != 0:
                result_set.append(value)

    elif choice == 3:
        for value in universal_set:
            if value > 0:
                result_set.append(value)

    elif choice == 4:
        for value in universal_set:
            if value < 0:
                result_set.append(value)

    elif choice == 5:
        limit = int(input("Enter the limit: "))

        for value in universal_set:
            if value > limit:
                result_set.append(value)

    elif choice == 6:
        limit = int(input("Enter the limit: "))

        for value in universal_set:
            if value < limit:
                result_set.append(value)

    elif choice == 7:
        divisor = int(input("Enter the divisor: "))

        if divisor == 0:
            print("Divisor cannot be zero.")
            return

        for value in universal_set:
            if value % divisor == 0:
                result_set.append(value)

    elif choice == 8:
        lower = int(input("Enter the lower limit: "))
        upper = int(input("Enter the upper limit: "))

        if lower > upper:
            print("Lower limit cannot be greater than upper limit.")
            return

        for value in universal_set:
            if lower <= value <= upper:
                result_set.append(value)

    else:
        print("Invalid choice.")
        return

    print("\nSet Builder Results :")
    print("Universal Set:", universal_set)
    print("Result Set:", result_set)
    print("Number of Elements in Universal Set:", len(universal_set))
    print("Number of Elements in Result Set:", len(result_set))

    if len(result_set) == 0:
        print("No elements satisfy the selected condition.")
    else:
        print("Elements satisfying the selected condition:")

        for value in result_set:
            print(value)

    print("\nSet Builder Representation:")
    print("A = {x in U | x satisfies the selected condition}")

setbuilderfromconditions()