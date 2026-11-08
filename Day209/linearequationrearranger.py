def linearequationrearranger():
    try:
        a = float(input("Enter coefficient of x: "))
        b = float(input("Enter coefficient of y: "))
        c = float(input("Enter constant value: "))

        print(f"\nOriginal Equation: {a}x + {b}y = {c}")

        print("\nRearranged Equation:")

        if b != 0:
            print(f"y = ({c} - {a}x) / {b}")
        else:
            print("Cannot rearrange for y because its coefficient is zero.")

        if a != 0:
            print(f"x = ({c} - {b}y) / {a}")
        else:
            print("Cannot rearrange for x because its coefficient is zero.")

    except ValueError:
        print("Please enter valid numeric coefficients.")

linearequationrearranger()