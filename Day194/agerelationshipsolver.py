def agerelationshipsolver():
    print("Age Relationship Solver :")

    try:
        age1 = int(input("Enter the current age of Person 1: "))
        age2 = int(input("Enter the current age of Person 2: "))
        years = int(input("Enter the number of years in the past or future: "))
    except ValueError:
        print("Invalid input! Please enter integers.")
        return

    if age1 < 0 or age2 < 0:
        print("Ages cannot be negative.")
        return

    print("\nCurrent Age Relationship :")
    print("Person 1 Age:", age1)
    print("Person 2 Age:", age2)

    if age1 > age2:
        print("Person 1 is older by", age1 - age2, "years.")
    elif age2 > age1:
        print("Person 2 is older by", age2 - age1, "years.")
    else:
        print("Both people are the same age.")

    print("\nChoose a relationship:")
    print("1. Ages in the past")
    print("2. Ages in the future")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        past_age1 = age1 - years
        past_age2 = age2 - years

        print("\nAges in the Past :")

        if past_age1 < 0 or past_age2 < 0:
            print("The selected time is before one or both people were born.")
        else:
            print("Person 1 Age:", past_age1)
            print("Person 2 Age:", past_age2)

            if past_age1 > past_age2:
                print("Person 1 was older by", past_age1 - past_age2, "years.")
            elif past_age2 > past_age1:
                print("Person 2 was older by", past_age2 - past_age1, "years.")
            else:
                print("Both people were the same age.")

    elif choice == "2":
        future_age1 = age1 + years
        future_age2 = age2 + years

        print("\nAges in the Future :")
        print("Person 1 Age:", future_age1)
        print("Person 2 Age:", future_age2)

        if future_age1 > future_age2:
            print("Person 1 will be older by", future_age1 - future_age2, "years.")
        elif future_age2 > future_age1:
            print("Person 2 will be older by", future_age2 - future_age1, "years.")
        else:
            print("Both people will be the same age.")

    else:
        print("Invalid choice! Please select 1 or 2.")
        return

    print("\nAge Ratio :")

    if age2 != 0:
        print("Current Age Ratio:", age1, ":", age2)
        print("Age Ratio Value:", round(age1 / age2, 2))
    elif age1 == 0:
        print("Age ratio is undefined because both ages are zero.")
    else:
        print("Age ratio is undefined because Person 2's age is zero.")

    print("\nAge Difference Verification :")
    print("Current Age Difference:", abs(age1 - age2), "years")

agerelationshipsolver()