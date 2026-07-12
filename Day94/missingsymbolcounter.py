def missingsymbol():
    total_objects = int(input("Enter total objects: "))
    value_per_symbol = int(input("Enter value of one symbol: "))

    symbols = total_objects // value_per_symbol

    print("Missing Symbols:", symbols)

missingsymbol()