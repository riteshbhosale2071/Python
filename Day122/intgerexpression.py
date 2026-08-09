def integerexpression():
    expression = input("Enter an integer expression: ")

    try:
        result = eval(expression, {"__builtins__": None}, {})

        if isinstance(result, (int, float)):
            print("Result:", result)
        else:
            print("Invalid expression.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except:
        print("Invalid expression.")

integerexpression()