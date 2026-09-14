def differenceofsquarespuzzle():
    print("Difference-of-Squares Puzzle :")

    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))

    print("\nExpression:")
    print(a, "^2 -", b, "^2")

    result = a * a - b * b
    factor1 = a + b
    factor2 = a - b

    print("\nUsing the identity:")
    print("a^2 - b^2 = (a + b)(a - b)")

    print("Factor 1:", factor1)
    print("Factor 2:", factor2)
    print("Result:", result)

    if factor1 * factor2 == result:
        print("Puzzle solved and verified!")
    else:
        print("Verification failed.")

differenceofsquarespuzzle()