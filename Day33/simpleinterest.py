def find():
    p = float(input("Enter Principal Amount: "))
    r = float(input("Enter Rate of Interest: "))
    t = float(input("Enter Time Period: "))

    si = (p * r * t) / 100

    print("Simple Interest =", si)

find()