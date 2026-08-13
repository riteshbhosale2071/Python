def rationalnumsign():
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        print("Denominator cannot be zero.")
        return

    if numerator == 0:
        print("The rational number is Zero.")
    elif (numerator > 0 and denominator > 0) or (numerator < 0 and denominator < 0):
        print("The rational number is Positive.")
    else:
        print("The rational number is Negative.")

rationalnumsign()