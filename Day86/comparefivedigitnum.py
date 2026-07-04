def compare():
    num1 = int(input("Enter the first five-digit number: "))
    num2 = int(input("Enter the second five-digit number: "))

    if not (10000 <= num1 <= 99999 and 10000 <= num2 <= 99999):
        print("Please enter valid five-digit numbers.")
        return

    print("\nComparison Result :")
    print("First Number  =", num1)
    print("Second Number =", num2)

    if num1 > num2:
        print(num1, "is greater than", num2)
    elif num1 < num2:
        print(num2, "is greater than", num1)
    else:
        print("Both numbers are equal.")

compare()