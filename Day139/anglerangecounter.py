def anglerangecounter():
    angles = list(map(float, input("Enter angles separated by spaces: ").split()))
    lower = float(input("Enter lower limit: "))
    upper = float(input("Enter upper limit: "))

    if not angles:
        print("Please enter at least one angle.")
        return

    if lower > upper:
        lower, upper = upper, lower

    count = 0

    for angle in angles:
        if lower <= angle <= upper:
            count += 1

    print("Number of angles in the range:", count)

anglerangecounter()