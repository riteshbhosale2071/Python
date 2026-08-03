def triangleinequality():
    a = float(input("Enter the first side: "))
    b = float(input("Enter the second side: "))
    c = float(input("Enter the third side: "))

    if (a + b > c) and (a + c > b) and (b + c > a):
        print("Triangle Inequality Satisfied.")
        print("A valid triangle can be formed.")
    else:
        print("Triangle Inequality Not Satisfied.")
        print("A valid triangle cannot be formed.")

triangleinequality()