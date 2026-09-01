def ratiomissingterm():
    print("Given ratio: a : b = c : d")
    print("Enter 0 for the missing term.")

    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    d = float(input("Enter d: "))

    if [a, b, c, d].count(0) != 1:
        print("Enter exactly one missing term as 0.")
        return

    if a == 0:
        if d == 0 or c == 0:
            print("Cannot calculate the missing term.")
            return
        a = (b * c) / d
        print("Missing term a:", a)

    elif b == 0:
        if c == 0:
            print("Cannot calculate the missing term.")
            return
        b = (a * d) / c
        print("Missing term b:", b)

    elif c == 0:
        if a == 0 or d == 0:
            print("Cannot calculate the missing term.")
            return
        c = (a * d) / b
        print("Missing term c:", c)

    elif d == 0:
        if a == 0:
            print("Cannot calculate the missing term.")
            return
        d = (b * c) / a
        print("Missing term d:", d)

ratiomissingterm()