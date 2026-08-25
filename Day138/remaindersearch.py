def remaindersearch():
    divisors = list(map(int, input(
        "Enter divisors separated by spaces: "
    ).split()))

    remainder = int(input("Enter the required common remainder: "))

    if not divisors or any(divisor <= 0 for divisor in divisors):
        print("Please enter positive divisors.")
        return

    if remainder < 0 or any(remainder >= divisor for divisor in divisors):
        print("Invalid remainder.")
        return

    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))

    if start > end:
        start, end = end, start

    found = []

    for number in range(start, end + 1):
        if all(number % divisor == remainder for divisor in divisors):
            found.append(number)

    if found:
        print("Numbers satisfying the condition:", found)
    else:
        print("No number found in the given range.")

remaindersearch()