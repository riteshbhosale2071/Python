def missingnum():
    product = int(input("Enter product: "))
    
    factor = int(input("Enter known factor: "))

    missing = product // factor

    print("Missing Factor =", missing)

missingnum()