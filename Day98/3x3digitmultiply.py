def multiplynumbers():
    num1 = int(input("Enter first 3-digit number: "))
    num2 = int(input("Enter second 3-digit number: "))
    
    if 100 <= num1 <= 999 and 100 <= num2 <= 999:
        print("Product =", num1 * num2)
    else:
        print("Please enter only three-digit numbers.")

multiplynumbers()