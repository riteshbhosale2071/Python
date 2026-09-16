def factorisationrule():
    print("Factorisation Rule Engine :")
    print("1. Common Factor")
    print("2. Difference of Squares")
    print("3. Perfect Square")
    print("4. Quadratic Expression")

    choice = int(input("Enter rule choice: "))

    if choice == 1:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        common = 1

        for i in range(1, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                common = i

        print("Rule: Take out the common factor.")
        print("Common factor =", common)

    elif choice == 2:
        a = int(input("Enter value of a: "))
        b = int(input("Enter value of b: "))

        print("Rule: a^2 - b^2 = (a + b)(a - b)")
        print("Factorised form = (", a + b, ")(", a - b, ")")

    elif choice == 3:
        a = int(input("Enter value of a: "))
        b = int(input("Enter value of b: "))

        print("Rule: a^2 + 2ab + b^2 = (a + b)^2")
        print("Factorised form = (", a + b, ")^2")

    elif choice == 4:
        a = int(input("Enter coefficient a: "))
        b = int(input("Enter coefficient b: "))
        c = int(input("Enter coefficient c: "))

        found = False

        for x in range(-100, 101):
            for y in range(-100, 101):
                if x * y == a * c and x + y == b:
                    print("Rule: Find two numbers whose product is a*c and sum is b.")
                    print("Required numbers =", x, "and", y)
                    found = True
                    break
            if found:
                break

        if not found:
            print("No suitable factorisation rule found.")

    else:
        print("Invalid choice.")

factorisationrule()