def factorpairs():
    number = int(input("Enter a number: "))
    print("Factor Pairs of", number, "are:")

    for i in range(1, number + 1):
        if number % i == 0:
            print(i, "x", number // i)

factorpairs()