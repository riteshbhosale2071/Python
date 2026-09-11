def polynomialtermcounter():
    print("Polynomial Term Counter :")

    polynomial = input("Enter a polynomial: ")

    terms = 0
    i = 0

    while i < len(polynomial):
        if polynomial[i] != " ":
            if i == 0:
                terms = terms + 1
            elif polynomial[i] == "+" or polynomial[i] == "-":
                terms = terms + 1
        i = i + 1

    print("Number of terms:", terms)

polynomialtermcounter()