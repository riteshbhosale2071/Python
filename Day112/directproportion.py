def directproportion():
    x = float(input("Enter the first value: "))
    y = float(input("Enter the second value: "))
    new_x = float(input("Enter the new first value: "))

    new_y = (y * new_x) / x

    print("New second value:", new_y)

directproportion()