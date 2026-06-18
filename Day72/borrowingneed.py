def subtraction():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    borrow_needed = False
    borrow = 0

    while num1 > 0 or num2 > 0:

        digit1 = (num1 % 10) - borrow
        digit2 = num2 % 10

        if digit1 < digit2:
            borrow_needed = True
            break

        borrow = 0
        num1 //= 10
        num2 //= 10

    if borrow_needed:
        print("Borrowing Needed")

    else:
        print("No Borrowing Needed")

subtraction()