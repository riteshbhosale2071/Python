def largest():
    digits = []

    print("Enter 5 digits:")

    for i in range(5):
        digit = int(input(f"Enter digit {i+1}: "))

        if 0 <= digit <= 9:
            digits.append(digit)
        else:
            print("Please enter a digit between 0 and 9.")
            return

    digits.sort(reverse=True)

    largest_number = ""

    for digit in digits:
        largest_number += str(digit)

    print("\nLargest Five-Digit Number")
    print("Largest Number =", largest_number)

largest()