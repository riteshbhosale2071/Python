def concurrentline():
    slope1 = int(input("Enter slope of first line: "))
    slope2 = int(input("Enter slope of second line: "))

    if slope1 == slope2:
        print("Lines are Parallel")
    else:
        print("Lines are Not Parallel")

concurrentline()