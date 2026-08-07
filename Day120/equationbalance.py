def equationbalance():
    left_side = float(input("Enter the value of the left side: "))
    right_side = float(input("Enter the value of the right side: "))

    if left_side == right_side:
        print("The equation is Balanced.")
    else:
        print("The equation is Not Balanced.")
        print("Difference:", abs(left_side - right_side))

equationbalance()