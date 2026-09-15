def factorisationerrordetector():
    print("Factorisation Error Detector :")

    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))

    correct = (a + b) * (a - b)
    given = int(input("Enter the value obtained from your factorisation: "))

    print("Original expression value =", a * a - b * b)
    print("Correct factorised value =", correct)
    print("Your factorised value =", given)

    if given == correct:
        print("No error detected. Factorisation is correct.")
    else:
        print("Error detected in factorisation.")
        print("Correct answer should be:", correct)

factorisationerrordetector()