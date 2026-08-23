def numberfactorcount():
    number = int(input("Enter a positive integer: "))

    if number <= 0:
        print("Please enter a positive integer.")
        return

    count = 0

    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    print("Number of Factors:", count)

numberfactorcount()