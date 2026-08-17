def proportionmissingvalue():
    print("Solve the proportion: a / b = c / d")
    
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    if b == 0:
        print("b cannot be zero.")
        return

    if a == 0:
        print("a cannot be zero for this calculation.")
        return

    d = (b * c) / a

    print("Missing Value:", d)

proportionmissingvalue()