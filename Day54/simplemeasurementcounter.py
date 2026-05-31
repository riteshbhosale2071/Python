def counter():
    while True:

        print("\n1. CM to Meter")
        print("2. Meter to KM")
        print("3. KG to Gram")
        print("4. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:

            cm = float(input("Enter CM: "))
            print("Meters =", cm / 100)

        elif choice == 2:

            m = float(input("Enter Meters: "))
            print("KM =", m / 1000)

        elif choice == 3:

            kg = float(input("Enter KG: "))
            print("Grams =", kg * 1000)

        elif choice == 4:
            break

        else:
            print("Invalid Choice")

counter()