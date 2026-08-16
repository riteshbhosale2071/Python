import re

def algebraicterm():
    expression = input("Enter an algebraic expression: ").replace(" ", "")

    if not expression:
        print("Please enter an expression.")
        return

    terms = re.findall(r'[+-]?(?:\d*\.?\d*)?[a-zA-Z](?:\^\d+)?|[+-]?\d+\.?\d*', expression)

    print("Terms:", terms)
    print("Number of Terms:", len(terms))

algebraicterm()