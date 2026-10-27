def conditionalstatement():
    print("Conditional Statement Converter")
    print("1. Convert age condition")
    print("2. Convert number condition")
    print("3. Convert marks condition")

    choice = input("Enter your choice: ")

    if choice == "1":
        age = int(input("Enter age: "))
        if age >= 18:
            print("if age >= 18: Eligible to vote")
        else:
            print("if age < 18: Not eligible to vote")

    elif choice == "2":
        number = int(input("Enter a number: "))
        if number % 2 == 0:
            print("if number % 2 == 0: Even number")
        else:
            print("if number % 2 != 0: Odd number")

    elif choice == "3":
        marks = float(input("Enter marks: "))
        if marks >= 40:
            print("if marks >= 40: Pass")
        else:
            print("if marks < 40: Fail")

    else:
        print("Invalid choice")

conditionalstatement()