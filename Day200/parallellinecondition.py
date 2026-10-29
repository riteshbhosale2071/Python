def parallellinecondition():
    print("Parallel Line Condition Checker")
    print("1. Check parallel lines using slopes")
    print("2. Check parallel lines using line equations")

    choice = input("Enter your choice: ")

    if choice == "1":
        m1 = float(input("Enter slope of first line: "))
        m2 = float(input("Enter slope of second line: "))

        if abs(m1 - m2) < 0.000001:
            print("The lines are parallel or coincident.")
        else:
            print("The lines are not parallel.")

    elif choice == "2":
        print("Enter equations in the form ax + by + c = 0")

        a1 = float(input("Enter a1: "))
        b1 = float(input("Enter b1: "))
        c1 = float(input("Enter c1: "))

        a2 = float(input("Enter a2: "))
        b2 = float(input("Enter b2: "))
        c2 = float(input("Enter c2: "))

        if a1 * b2 == a2 * b1:
            if a1 * c2 == a2 * c1 and b1 * c2 == b2 * c1:
                print("The lines are coincident.")
            else:
                print("The lines are parallel.")
        else:
            print("The lines are not parallel.")

    else:
        print("Invalid choice.")

parallellinecondition()