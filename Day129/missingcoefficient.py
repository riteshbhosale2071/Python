import re

def missingcoefficient():
    term = input("Enter an algebraic term with missing coefficient (e.g., ?x^2): ")
    term = term.replace(" ", "")

    match = re.fullmatch(r'\?([a-zA-Z](?:\^\d+)?)', term)

    if match:
        variable_part = match.group(1)
        print("Missing Coefficient: 1")
        print("Completed Term:", "1" + variable_part)
    else:
        print("Invalid format. Use ? followed by a variable, e.g., ?x^2.")

missingcoefficient()