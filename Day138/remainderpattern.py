def remainderpattern():
    divisor = int(input("Enter the divisor: "))
    terms = int(input("Enter the number of terms: "))

    if divisor <= 0 or terms <= 0:
        print("Divisor and number of terms must be positive.")
        return

    print("Remainder Pattern:")

    for number in range(1, terms + 1):
        remainder = number % divisor
        print(f"{number} % {divisor} = {remainder}")

remainderpattern()