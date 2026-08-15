def bardifferencecalc():
    values = list(map(int, input("Enter bar values separated by spaces: ").split()))

    if len(values) < 2:
        print("Enter at least two bar values.")
        return

    maximum = max(values)
    minimum = min(values)
    difference = maximum - minimum

    print("Maximum Bar Value:", maximum)
    print("Minimum Bar Value:", minimum)
    print("Difference:", difference)

bardifferencecalc()