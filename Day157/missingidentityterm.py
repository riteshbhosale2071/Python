def missingidentityterm():
    print("Missing Identity Term Finder :")
    print("1. (a + b)^2 = a^2 + ? + b^2")
    print("2. (a - b)^2 = a^2 - ? + b^2")
    print("3. a^2 - b^2 = (a + b)(?)")
    print("4. (a + b)^3 = a^3 + 3a^2b + ? + b^3")
    print("5. (a - b)^3 = a^3 - 3a^2b + ? - b^3")

    choice = int(input("\nEnter identity number: "))

    if choice == 1:
        print("Missing term: 2ab")

    elif choice == 2:
        print("Missing term: 2ab")

    elif choice == 3:
        print("Missing term: a - b")

    elif choice == 4:
        print("Missing term: 3ab^2")

    elif choice == 5:
        print("Missing term: 3ab^2")

    else:
        print("Invalid identity number.")

missingidentityterm()