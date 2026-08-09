def wordproblemequation():
    print("Word Problem Equation Solver")
    print("Example: A number increased by a value equals a result.")
    
    number = float(input("Enter the known number: "))
    increase = float(input("Enter the increase/decrease value: "))
    result = float(input("Enter the final result: "))

    if increase >= 0:
        x = result - increase
        print(f"Equation: x + {increase} = {result}")
    else:
        x = result - increase
        print(f"Equation: x - {abs(increase)} = {result}")

    print("Missing value:", round(x, 2))

wordproblemequation()