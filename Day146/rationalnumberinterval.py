def rationalnumberinterval():
    start = int(input("Enter starting numerator: "))
    end = int(input("Enter ending numerator: "))
    denominator = int(input("Enter denominator: "))

    if denominator == 0:
        print("Denominator cannot be zero.")
        return

    if start > end:
        start, end = end, start

    print("\nRational Number Interval :")

    for numerator in range(start, end + 1):
        value = numerator / denominator
        print(f"{numerator}/{denominator} = {value}")

rationalnumberinterval()