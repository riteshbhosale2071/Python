def digitsmultiply():
    num1 = int(input("Enter a three-digit number: "))
    num2 = int(input("Enter a one-digit number: "))

    if not (100 <= num1 <= 999):
        print("Please enter a valid three-digit number.")
        return

    if not (0 <= num2 <= 9):
        print("Please enter a valid one-digit number.")
        return

    hundreds = num1 // 100
    tens = (num1 // 10) % 10
    ones = num1 % 10

    print("\nStepwise Multiplication")
    print("-" * 35)

    print(f"Hundreds: {hundreds} × {num2} × 100 = {hundreds * num2 * 100}")
    print(f"Tens     : {tens} × {num2} × 10  = {tens * num2 * 10}")
    print(f"Ones     : {ones} × {num2} × 1   = {ones * num2}")

    product = num1 * num2

    print("-" * 35)
    print("Final Product =", product)

digitsmultiply()