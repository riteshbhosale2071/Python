def find():
    p = float(input("Enter Principal Amount: "))
    r = float(input("Enter Rate of Interest: "))
    t = float(input("Enter Time Period: "))

    amount = p * (1 + r / 100) ** t

    ci = amount - p

    print("Compound Interest =", ci)
    print("Total Amount =", amount)

find()