def remainderpattern():
    numbers = list(map(int, input("Enter divisors separated by spaces: ").split()))
    remainder = int(input("Enter the common remainder: "))

    if not numbers or any(number <= 0 for number in numbers):
        print("Please enter positive divisors.")
        return

    if any(remainder >= number for number in numbers) or remainder < 0:
        print("Invalid remainder.")
        return

    candidate = remainder

    while True:
        if all(candidate % number == remainder for number in numbers):
            print("Smallest Number:", candidate)
            break
        candidate += 1

remainderpattern()