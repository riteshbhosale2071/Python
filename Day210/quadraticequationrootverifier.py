def quadraticequationrootverifier():
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))

        if a == 0:
            print("Invalid quadratic equation.")
            return

        root1 = float(input("Enter first proposed root: "))
        root2 = float(input("Enter second proposed root: "))

        result1 = a * root1 ** 2 + b * root1 + c
        result2 = a * root2 ** 2 + b * root2 + c

        print("\nEquation: ax² + bx + c = 0")
        print("First Root Result:", round(result1, 4))
        print("Second Root Result:", round(result2, 4))

        if abs(result1) < 1e-9:
            print("First root is correct.")
        else:
            print("First root is incorrect.")

        if abs(result2) < 1e-9:
            print("Second root is correct.")
        else:
            print("Second root is incorrect.")

        if abs(result1) < 1e-9 and abs(result2) < 1e-9:
            print("Both proposed roots are verified.")
        else:
            print("The proposed roots are not both correct.")

    except ValueError:
        print("Please enter valid numeric values.")

quadraticequationrootverifier()