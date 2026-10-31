def constructionconditionselector():
    print("Triangle Construction Conditions")
    print("1. SSS - Three sides")
    print("2. SAS - Two sides and included angle")
    print("3. ASA - Two angles and included side")
    print("4. AAS - Two angles and a non-included side")
    print("5. RHS - Right angle, hypotenuse, and one side")

    choice = input("Select a construction condition (1-5): ")

    conditions = {
        "1": "SSS - Three sides",
        "2": "SAS - Two sides and included angle",
        "3": "ASA - Two angles and included side",
        "4": "AAS - Two angles and a non-included side",
        "5": "RHS - Right angle, hypotenuse, and one side"
    }

    if choice in conditions:
        print("Selected condition:", conditions[choice])
    else:
        print("Invalid selection. Choose a number from 1 to 5.")

constructionconditionselector()