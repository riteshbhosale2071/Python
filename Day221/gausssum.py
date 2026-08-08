def gausssum():
    n = int(input("Enter the value of N: "))

    if n < 1:
        print("Please enter a positive integer.")
        return

    total = n * (n + 1) // 2

    print("Sum of numbers from 1 to", n, "is:", total)

gausssum()