def algebrastepverification():
    print("Algebra Step Verification :")

    print("\nSolve a linear equation in the form:")
    print("a x + b = c")

    a = float(input("Enter coefficient of x: "))
    b = float(input("Enter constant: "))
    c = float(input("Enter right-side value: "))

    if a == 0:
        if b == c:
            print("\nThe equation has infinitely many solutions.")
        else:
            print("\nThe equation has no solution.")
        return

    solution = (c - b) / a

    print("\nStep Verification :")

    print("Step 1:")
    print(a, "x +", b, "=", c)

    print("\nStep 2: Subtract", b, "from both sides.")
    print(a, "x =", c - b)

    print("\nStep 3: Divide both sides by", a)
    print("x =", round(solution, 2))

    left_side = a * solution + b
    right_side = c

    print("\nVerification :")
    print("Left Side:", round(left_side, 2))
    print("Right Side:", round(right_side, 2))

    if abs(left_side - right_side) < 0.000001:
        print("Verification: Correct")
        print("The solution satisfies the original equation.")
    else:
        print("Verification: Incorrect")

algebrastepverification()