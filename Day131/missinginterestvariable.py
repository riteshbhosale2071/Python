def missinginterestvariable():
    print("Simple Interest Formula: SI = (P × R × T) / 100")

    choice = input("Enter the missing variable (P/R/T): ").upper()
    si = float(input("Enter Simple Interest: "))

    if choice == "P":
        rate = float(input("Enter Rate (%): "))
        time = float(input("Enter Time (years): "))

        if rate <= 0 or time <= 0:
            print("Rate and time must be positive.")
            return

        principal = (si * 100) / (rate * time)
        print("Missing Principal:", principal)

    elif choice == "R":
        principal = float(input("Enter Principal: "))
        time = float(input("Enter Time (years): "))

        if principal <= 0 or time <= 0:
            print("Principal and time must be positive.")
            return

        rate = (si * 100) / (principal * time)
        print("Missing Rate:", rate, "%")

    elif choice == "T":
        principal = float(input("Enter Principal: "))
        rate = float(input("Enter Rate (%): "))

        if principal <= 0 or rate <= 0:
            print("Principal and rate must be positive.")
            return

        time = (si * 100) / (principal * rate)
        print("Missing Time:", time, "years")

    else:
        print("Invalid choice. Enter P, R, or T.")

missinginterestvariable()