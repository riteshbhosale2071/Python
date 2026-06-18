def check():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    carry_needed = False

    while num1 > 0 or num2 > 0:

        digit1 = num1 % 10
        digit2 = num2 % 10

        if digit1 + digit2 >= 10:
            carry_needed = True
            break

        num1 //= 10
        num2 //= 10

    if carry_needed:
        print("Carry Needed")

    else:
        print("No Carry Needed")

check()