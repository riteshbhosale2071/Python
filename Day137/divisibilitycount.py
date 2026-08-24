def divisibilitycount():
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))
    divisor = int(input("Enter the divisor: "))

    if divisor == 0:
        print("Divisor cannot be zero.")
        return

    if start > end:
        start, end = end, start

    count = 0

    for number in range(start, end + 1):
        if number % divisor == 0:
            count += 1

    print("Count of Divisible Numbers:", count)

divisibilitycount()