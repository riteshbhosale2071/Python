def algebraicexpressionevaluator():
    expression = input("Enter an algebraic expression: ")
    variables = {}

    for variable in set(expression):
        if variable.isalpha():
            variables[variable] = float(
                input(f"Enter value of {variable}: ")
            )

    try:
        result = eval(expression, {"__builtins__": None}, variables)
        print("Expression Value:", result)
    except:
        print("Invalid algebraic expression.")

algebraicexpressionevaluator()