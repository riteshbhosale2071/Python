def smallest():
    digits = []

    print("Enter 5 digits:")

    for i in range(5):
        digit = int(input(f"Enter digit {i+1}: "))

        if 0 <= digit <= 9:
            digits.append(digit)
        else:
            print("Please enter a digit between 0 and 9.")
            return

    digits.sort()

    # Ensure the number does not start with 0
    if digits[0] == 0:
        for i in range(1, 5):
            if digits[i] != 0:
                digits[0], digits[i] = digits[i], digits[0]
                break

    smallest_number = ""

    for digit in digits:
        smallest_number += str(digit)

    print("\nSmallest Five-Digit Number")
    print("-" * 30)
    print("Smallest Number =", smallest_number)

smallest()