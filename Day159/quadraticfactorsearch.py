def quadraticfactorsearch():
    print("Quadratic Factor Search :")

    a = int(input("Enter coefficient a: "))
    b = int(input("Enter coefficient b: "))
    c = int(input("Enter coefficient c: "))

    found = False

    for x in range(-100, 101):
        for y in range(-100, 101):
            if x * y == a * c and x + y == b:
                print("Middle terms:", x, "and", y)
                print("Quadratic factorisation can be formed using these values.")
                found = True
                break
        if found:
            break

    if not found:
        print("No suitable factor pair found.")

quadraticfactorsearch()