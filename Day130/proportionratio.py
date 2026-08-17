import math

def proportionratio():
    first = int(input("Enter first ratio value: "))
    second = int(input("Enter second ratio value: "))

    if first <= 0 or second <= 0:
        print("Please enter positive integers.")
        return

    common_factor = math.gcd(first, second)

    simplified_first = first // common_factor
    simplified_second = second // common_factor

    print("Original Ratio:", f"{first}:{second}")
    print("Simplified Ratio:", f"{simplified_first}:{simplified_second}")

proportionratio()