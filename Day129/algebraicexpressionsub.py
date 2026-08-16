import re

def algebraicexpressionsub():
    expression1 = input("Enter first algebraic expression: ")
    expression2 = input("Enter second algebraic expression: ")

    def parse_expression(expression):
        expression = expression.replace(" ", "")
        terms = re.findall(r'[+-]?\d*[a-zA-Z](?:\^\d+)?|[+-]?\d+', expression)
        groups = {}

        for term in terms:
            match = re.match(r'([+-]?\d*)([a-zA-Z]?)(?:\^(\d+))?', term)

            coefficient, variable, exponent = match.groups()

            if coefficient in ("", "+"):
                coefficient = 1
            elif coefficient == "-":
                coefficient = -1
            else:
                coefficient = int(coefficient)

            key = (variable, exponent if exponent else "1" if variable else "0")
            groups[key] = groups.get(key, 0) + coefficient

        return groups

    result = parse_expression(expression1)

    for key, value in parse_expression(expression2).items():
        result[key] = result.get(key, 0) - value

    output = []

    for (variable, exponent), coefficient in result.items():
        if coefficient == 0:
            continue

        if variable:
            if coefficient == 1:
                term = variable
            elif coefficient == -1:
                term = "-" + variable
            else:
                term = f"{coefficient}{variable}"

            if exponent != "1":
                term += f"^{exponent}"
        else:
            term = str(coefficient)

        output.append(term)

    simplified = " + ".join(output).replace("+ -", "- ")

    print("Difference of Expressions:", simplified)

algebraicexpressionsub()