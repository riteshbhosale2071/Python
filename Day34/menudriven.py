while True:
    print("\n--- MENU ---")
    print("1. CM to FT")
    print("2. KM to Miles")
    print("3. USD to INR")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        cm = float(input("Enter value in CM: "))
        ft = cm / 30.48
        print("Feet =", ft)
    elif choice == 2:
        km = float(input("Enter value in KM: "))
        miles = km * 0.621371
        print("Miles =", miles)
    elif choice == 3:
        usd = float(input("Enter USD: "))
        inr = usd * 83
        print("INR =", inr)
    elif choice == 4:
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice")