import re

def monomialmultiplication():
    term1 = input("Enter first monomial (e.g., 3x^2): ")
    term2 = input("Enter second monomial (e.g., 4x^3): ")

    def parse_monomial(term):
        term = term.replace(" ", "")
        match = re.fullmatch(r'([+-]?\d*\.?\d*)([a-zA-Z]?)(?:\^(\d+))?', term)

        if not match:
            return None

        coefficient, variable, exponent = match.groups()

        if coefficient in ("", "+"):
            coefficient = 1
        elif coefficient == "-":
            coefficient = -1
        else:
            coefficient = float(coefficient)

        exponent = int(exponent) if exponent else (1 if variable else 0)

        return coefficient, variable, exponent

    monomial1 = parse_monomial(term1)
    monomial2 = parse_monomial(term2)

    if monomial1 is None or monomial2 is None:
        print("Invalid monomial.")
        return

    coefficient1, variable1, exponent1 = monomial1
    coefficient2, variable2, exponent2 = monomial2

    if variable1 != variable2 and variable1 and variable2:
        print("Monomials have different variables.")
        return

    coefficient = coefficient1 * coefficient2
    variable = variable1 or variable2
    exponent = exponent1 + exponent2

    if coefficient == int(coefficient):
        coefficient = int(coefficient)

    if variable:
        if coefficient == 1:
            result = variable
        elif coefficient == -1:
            result = "-" + variable
        else:
            result = f"{coefficient}{variable}"

        if exponent != 1:
            result += f"^{exponent}"
    else:
        result = str(coefficient)

    print("Product:", result)

monomialmultiplication()