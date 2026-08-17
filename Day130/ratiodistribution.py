def ratiodistribution():
    total = float(input("Enter the total amount: "))
    ratio1 = int(input("Enter first ratio value: "))
    ratio2 = int(input("Enter second ratio value: "))

    if total < 0 or ratio1 <= 0 or ratio2 <= 0:
        print("Please enter valid positive values.")
        return

    total_ratio = ratio1 + ratio2

    first_share = (ratio1 / total_ratio) * total
    second_share = (ratio2 / total_ratio) * total

    print("Ratio:", f"{ratio1}:{ratio2}")
    print("First Share:", first_share)
    print("Second Share:", second_share)

ratiodistribution()