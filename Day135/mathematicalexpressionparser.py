def mathematicalexpressionparser():
    expression = input("Enter a mathematical expression: ")

    try:
        # Remove spaces
        expression = expression.replace(" ", "")

        # Evaluate the expression
        result = eval(expression, {"__builtins__": None}, {})

        print("Expression:", expression)
        print("Result:", result)

    except:
        print("Invalid mathematical expression.")

mathematicalexpressionparser()