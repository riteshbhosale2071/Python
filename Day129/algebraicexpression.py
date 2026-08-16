import re

def algebraicexpression():
    expression = input("Enter algebraic expression (e.g., 3x + 5x - 2): ")

    expression = expression.replace(" ", "")
    terms = re.findall(r'[+-]?\d*\.?\d*[a-zA-Z](?:\^\d+)?|[+-]?\d+\.?\d*', expression)

    groups = {}

    for term in terms:
        match = re.match(r'([+-]?\d*\.?\d*)([a-zA-Z]?)(?:\^(\d+))?', term)

        if not match:
            continue

        coefficient, variable, exponent = match.groups()

        if coefficient in ("", "+"):
            coefficient = 1
        elif coefficient == "-":
            coefficient = -1
        else:
            coefficient = float(coefficient)

        exponent = exponent if exponent else ("1" if variable else "0")
        key = (variable, exponent)

        groups[key] = groups.get(key, 0) + coefficient

    result = []

    for (variable, exponent), coefficient in groups.items():
        if coefficient == 0:
            continue

        coefficient = int(coefficient) if coefficient == int(coefficient) else coefficient

        if variable:
            if coefficient == 1:
                term = variable
            elif coefficient == -1:
                term = "-" + variable
            else:
                term = str(coefficient) + variable

            if exponent != "1":
                term += "^" + exponent
        else:
            term = str(coefficient)

        result.append(term)

    simplified = " + ".join(result).replace("+ -", "- ")

    print("Simplified Expression:", simplified)

algebraicexpression()