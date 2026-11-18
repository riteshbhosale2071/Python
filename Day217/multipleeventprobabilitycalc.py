def multipleeventprobabilitycalc():
    print("Multiple Event Probability Calculator")

    print("\nSelect Probability Operation:")
    print("1. Probability of A or B")
    print("2. Probability of A and B")
    print("3. Probability of Neither A nor B")
    print("4. Conditional Probability")
    print("5. Complementary Probability")

    choice = int(input("Enter your choice: "))

    if choice not in range(1, 6):
        print("Invalid choice.")
        return

    probability_a = float(input("Enter probability of event A: "))

    if not 0 <= probability_a <= 1:
        print("Probability must be between 0 and 1.")
        return

    if choice == 5:
        result = 1 - probability_a

    else:
        probability_b = float(input("Enter probability of event B: "))

        if not 0 <= probability_b <= 1:
            print("Probability must be between 0 and 1.")
            return

        if choice == 1:
            probability_ab = float(input("Enter probability of A and B: "))
            result = probability_a + probability_b - probability_ab

        elif choice == 2:
            independent = input("Are the events independent? (Yes/No): ").strip().lower()

            if independent == "yes":
                result = probability_a * probability_b
            elif independent == "no":
                conditional = float(input("Enter P(B|A): "))
                result = probability_a * conditional
            else:
                print("Invalid choice.")
                return

        elif choice == 3:
            probability_ab = float(input("Enter probability of A and B: "))
            result = 1 - (probability_a + probability_b - probability_ab)

        elif choice == 4:
            probability_ab = float(input("Enter probability of A and B: "))

            if probability_b == 0:
                print("Conditional probability is undefined.")
                return

            result = probability_ab / probability_b

        if choice in [1, 3, 4] and not 0 <= probability_ab <= min(probability_a, probability_b):
            print("Invalid intersection probability.")
            return

    if not 0 <= result <= 1:
        print("Invalid probability values.")
        return

    print("\nMultiple Event Probability Result:")
    print("Calculated Probability:", round(result, 4))
    print("Probability Percentage:", round(result * 100, 2), "%")

multipleeventprobabilitycalc()