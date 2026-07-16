def multiply():
    num1 = int(input("Enter a 4-digit number: "))
    num2 = int(input("Enter a 3-digit number: "))

    if 1000 <= num1 <= 9999 and 100 <= num2 <= 999:
        print("Product =", num1 * num2)
    else:
        print("Invalid input! Enter a 4-digit number and a 3-digit number.")

multiply()