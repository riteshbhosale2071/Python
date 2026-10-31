def triangleconstructionerror():
    try:
        a = float(input("Enter first side length: "))
        b = float(input("Enter second side length: "))
        c = float(input("Enter third side length: "))

        if a <= 0 or b <= 0 or c <= 0:
            print("Error: Side lengths must be positive.")
        elif a + b <= c:
            print("Error: Sum of first and second sides must be greater than the third side.")
        elif a + c <= b:
            print("Error: Sum of first and third sides must be greater than the second side.")
        elif b + c <= a:
            print("Error: Sum of second and third sides must be greater than the first side.")
        else:
            print("No construction errors detected. A valid triangle can be constructed.")

    except ValueError:
        print("Error: Please enter valid numeric side lengths.")

triangleconstructionerror()