def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def fractionsimplification():
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    gcd = find_gcd(numerator, denominator)

    if gcd == 1:
        print("The fraction is already in simplest form.")
    else:
        print("The fraction can be simplified.")
        print("Simplified Fraction:", numerator // gcd, "/", denominator // gcd)

fractionsimplification()