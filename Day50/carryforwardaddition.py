def create():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    carry = 0

    while a > 0 or b > 0:

        d1 = a % 10
        d2 = b % 10

        if d1 + d2 + carry >= 10:
            carry = 1
            print("Carry Generated")

        else:
            carry = 0

        a //= 10
        b //= 10

create()