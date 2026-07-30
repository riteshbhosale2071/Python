def missingratio():
    a = int(input("Enter the first value of the first ratio: "))
    b = int(input("Enter the second value of the first ratio: "))
    c = int(input("Enter the first value of the second ratio: "))

    missing = (b * c) // a

    print("Missing value:", missing)

missingratio()