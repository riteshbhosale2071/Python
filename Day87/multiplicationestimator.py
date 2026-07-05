def estimator():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    rounded_num1 = round(num1, -1)
    rounded_num2 = round(num2, -1)

    estimated_product = rounded_num1 * rounded_num2
    actual_product = num1 * num2

    print("\nMultiplication Estimation Report")
    print("-" * 40)
    print("First Number       =", num1)
    print("Second Number      =", num2)
    print("Rounded Numbers    =", rounded_num1, "and", rounded_num2)
    print("Estimated Product  =", estimated_product)
    print("Actual Product     =", actual_product)

estimator()