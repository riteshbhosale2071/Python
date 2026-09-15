def factorpairsearch():
    print("Factor Pair Search :")

    number = int(input("Enter a number: "))

    print("Factor pairs:")

    found = False

    for i in range(1, number + 1):
        if number % i == 0:
            pair = number // i
            if i <= pair:
                print(i, "x", pair)
                found = True

    if found:
        print("Factor pair search completed.")
    else:
        print("No factor pairs found.")

factorpairsearch()