def create():
    a = int(input("Enter bigger number: "))
    b = int(input("Enter smaller number: "))

    borrow = 0

    while a > 0 or b > 0:

        d1 = a % 10
        d2 = b % 10

        d1 = d1 - borrow

        if d1 < d2:
            print("Borrow Taken")
            borrow = 1

        else:
            borrow = 0

        a //= 10
        b //= 10

create()