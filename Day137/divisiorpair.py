def divisorpair():
    number = int(input("Enter a positive integer: "))

    if number <= 0:
        print("Please enter a positive integer.")
        return

    print("Divisor Pairs:")

    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            j = number // i
            print(f"({i}, {j})")

divisorpair()