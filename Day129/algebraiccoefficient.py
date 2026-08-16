import re

def algebraiccoefficient():
    term = input("Enter an algebraic term (e.g., -5x^2): ").strip()

    match = re.fullmatch(r'([+-]?\d*\.?\d*)([a-zA-Z](?:\^\d+)?)?', term)

    if not match:
        print("Invalid algebraic term.")
        return

    coefficient = match.group(1)

    if coefficient in ("", "+"):
        coefficient = 1
    elif coefficient == "-":
        coefficient = -1
    else:
        coefficient = float(coefficient)
        if coefficient.is_integer():
            coefficient = int(coefficient)

    print("Coefficient:", coefficient)

algebraiccoefficient()