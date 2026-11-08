def orderedpair():
    try:
        x_start = int(input("Enter starting value of x: "))
        x_end = int(input("Enter ending value of x: "))
        y_start = int(input("Enter starting value of y: "))
        y_end = int(input("Enter ending value of y: "))

        if x_start > x_end or y_start > y_end:
            print("Invalid range. Starting values must be smaller.")
            return

        print("\nGenerated Ordered Pairs:")
        count = 0

        for x in range(x_start, x_end + 1):
            for y in range(y_start, y_end + 1):
                print(f"({x}, {y})")
                count += 1

        print("\nTotal Ordered Pairs:", count)

    except ValueError:
        print("Please enter valid integer values.")

orderedpair()