def borrow():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    borrow_count = 0
    borrow = 0

    while num1 > 0 or num2 > 0:

        digit1 = (num1 % 10) - borrow
        digit2 = num2 % 10

        if digit1 < digit2:
            borrow_count += 1
            borrow = 1
        else:
            borrow = 0

        num1 //= 10
        num2 //= 10

    print("Total Borrowings =", borrow_count)

borrow()