def factorisationstep():
    print("Factorisation Step Generator :")

    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))

    expression = a * a - b * b

    print("Step 1: Write the expression")
    print(a, "^2 -", b, "^2")

    print("Step 2: Identify the difference of squares identity")
    print("a^2 - b^2 = (a + b)(a - b)")

    print("Step 3: Substitute the values")
    print("(", a, "+", b, ")(", a, "-", b, ")")

    print("Step 4: Simplified factorised form")
    print("(", a + b, ")(", a - b, ")")

    print("Step 5: Verification")
    print("Original value =", expression)
    print("Factorised value =", (a + b) * (a - b))

factorisationstep()