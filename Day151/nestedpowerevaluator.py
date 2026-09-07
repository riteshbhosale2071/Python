def nestedpowerevaluator():
    print("Nested Power Evaluator :")
    print("Expression format: (base^exponent1)^exponent2")

    base = float(input("Enter the base: "))
    exponent1 = int(input("Enter inner exponent: "))
    exponent2 = int(input("Enter outer exponent: "))

    if base == 0 and exponent1 < 0:
        print("Zero cannot have a negative exponent.")
        return

    if base == 0 and exponent1 == 0:
        print("0^0 is undefined.")
        return

    if base == 0 and exponent1 > 0 and exponent2 < 0:
        print("A zero result cannot have a negative outer exponent.")
        return

    inner_value = base ** exponent1
    final_value = inner_value ** exponent2

    simplified_exponent = exponent1 * exponent2

    print("\nNested Power Evaluation :")
    print(f"Original Expression: ({base}^{exponent1})^{exponent2}")
    print("Inner Value:", inner_value)
    print("Final Value:", final_value)

    print("\nUsing the Power-of-a-Power Rule:")
    print(f"({base}^{exponent1})^{exponent2} = {base}^{simplified_exponent}")

    print("Simplified Exponent:", simplified_exponent)
    print("Simplified Value:", base ** simplified_exponent)

nestedpowerevaluator()