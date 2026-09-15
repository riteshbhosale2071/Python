def factorisationverification():
    print("Factorisation Verification Engine :")

    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))

    print("Expression: a^2 - b^2")
    print("Factorised form: (a + b)(a - b)")

    original = a * a - b * b
    factorised = (a + b) * (a - b)

    print("Original expression =", original)
    print("Factorised expression =", factorised)

    if original == factorised:
        print("Factorisation verified successfully.")
    else:
        print("Factorisation is incorrect.")

factorisationverification()