def conversestatement():
    print("Converse Statement Generator")
    print("Format: If P, then Q")

    p = input("Enter statement P: ")
    q = input("Enter statement Q: ")

    print("\nOriginal Statement:")
    print("If", p + ", then", q + ".")

    print("\nConverse Statement:")
    print("If", q + ", then", p + ".")

conversestatement()