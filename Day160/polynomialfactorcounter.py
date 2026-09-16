def polynomialfactorcounter():
    print("Polynomial Factor Counter :")

    degree = int(input("Enter degree of polynomial: "))

    count = 0

    for i in range(degree + 1):
        coefficient = int(input("Enter coefficient for x^" + str(i) + ": "))

        if coefficient != 0:
            count += 1

    print("Number of non-zero factors/terms =", count)

polynomialfactorcounter()