def compareweight():
    weight1 = float(input("Enter first weight: "))
    weight2 = float(input("Enter second weight: "))

    if weight1 > weight2:
        print("First weight is heavier.")
    elif weight2 > weight1:
        print("Second weight is heavier.")
    else:
        print("Both weights are equal.")

compareweight()