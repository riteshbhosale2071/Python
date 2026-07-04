def multiplythreedigittwodigit():
    num1 = int(input("Enter a three-digit number: "))
    num2 = int(input("Enter a two-digit number: "))

    if not (100 <= num1 <= 999):
        print("Please enter a valid three-digit number.")
        return

    if not (10 <= num2 <= 99):
        print("Please enter a valid two-digit number.")
        return

    ones = num2 % 10
    tens = num2 // 10

    partial1 = num1 * ones
    partial2 = num1 * tens * 10
    product = partial1 + partial2

    print("\nStepwise Multiplication")
    print("-" * 35)
    print(f"{num1} × {ones} = {partial1}")
    print(f"{num1} × {tens} × 10 = {partial2}")
    print("-" * 35)
    print("Final Product =", product)

multiplythreedigittwodigit()