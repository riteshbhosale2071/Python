import sympy as sp

def algebraicexpressionequivalence():
    expression1 = input("Enter the first algebraic expression: ")
    expression2 = input("Enter the second algebraic expression: ")

    try:
        expr1 = sp.sympify(expression1)
        expr2 = sp.sympify(expression2)

        difference = sp.simplify(expr1 - expr2)

        print("First Expression:", expr1)
        print("Second Expression:", expr2)

        if difference == 0:
            print("The expressions are Equivalent.")
        else:
            print("The expressions are Not Equivalent.")

    except:
        print("Invalid algebraic expression.")

algebraicexpressionequivalence()